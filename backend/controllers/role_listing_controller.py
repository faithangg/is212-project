from flask import request, jsonify
from database import db
from datetime import datetime
from sqlalchemy import or_
import re
from models.role_listing import RoleListing
from models.role_skill import RoleSkill 
from models.role import Role 
from models.job_application import JobApplication
from models.category import Category
from models.staff import Staff
from blueprints.hr_blueprint import hr_blueprint
from blueprints.staff_blueprint import staff_blueprint
from models.staff_skill import StaffSkill
from .role_skill_match_controller import role_skill_match

# HELPER FUNCTION TO GET SKILLS BY ROLE NAME
def get_skills_by_role(role_name):
    try:
        skills_result = RoleSkill.query.filter_by(role_name=role_name).all()
        skills_list = [skill.skill_name for skill in skills_result]
        return skills_list
    except Exception as e:
        return [] 

# HELPER FUNCTION TO FILTER LISTINGS BY STAFF AND DEADLINE       
def filter_listings_by_staff_and_deadline(query, staff_id):
    # Get listing_ids the staff has applied for
    applied_listings = [application.listing_id for application in JobApplication.query.filter_by(staff_id=staff_id).all()]

    # Get the current date
    current_date = datetime.now().date()

    # Filter the query by listings staff has not applied and listings that has not passed deadline
    filtered_query = query.filter(
        ~RoleListing.listing_id.in_(applied_listings),
        RoleListing.deadline >= current_date
    )
    
    return filtered_query

# HELPER FUNCTION TO GET ROLE SKILL MATCH
def role_skill_match(staff_id, role_name):
    try:
        # Get all the skills based on the roles
        role_skills = [rs.skill_name for rs in RoleSkill.query.filter_by(role_name=role_name).all()]

        # Get all the skills that the staff has
        staff_skills = [ss.skill_name for ss in StaffSkill.query.filter_by(staff_id=staff_id).all()]

        # Determine skills that staff have and don't have based on the role's requirements
        staff_have = [skill for skill in role_skills if skill in staff_skills]
        staff_dont = [skill for skill in role_skills if skill not in staff_skills]

        # Calculate the percentage of roles matched
        if len(staff_have) + len(staff_dont) == 0:
            match_percentage = 0
        else:
            match_percentage = round((len(staff_have) / (len(staff_have) + len(staff_dont))) * 100)

        return {
            "code": 200,
            "data": {
                "have": staff_have,
                "dont": staff_dont,
                "match_percentage": str(match_percentage)
            }
        }
    except Exception as e:
        # Return an error in a dictionary format
        return {
            "code": 500,
            "error": str(e)
        }

####################################################################################################################################

# HR: GET ALL ROLE LISTINGS
@hr_blueprint.route('/role_listings', methods=['GET'])
def get_all_role_listings():
    
    try:
        # Get all the records from the database
        role_listings = RoleListing.query.all()



        role_data = []
        for listing in role_listings:
            listing_data = listing.json()
            role_name = listing.role_name
            role_desc = Role.query.filter_by(role_name=role_name).first()
            skills = get_skills_by_role(role_name)
            listing_data['skills_required'] = skills
            listing_data['role_desc'] = role_desc.role_desc
            role_data.append(listing_data)
        
        # If have records return the records
        if len(role_listings):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "role_listing": [listing for listing in role_data]
                    }
                }
            )
        
        # If not return 404 - nothing found
        return jsonify(
            {
                "code": 404,
                "message": "There are no role listings"
            }
        ), 404
        
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

# HR: GET A SPECIFIC ROLE LISTING
@hr_blueprint.route('/role_listings/<string:listing_id>', methods=['GET'])
def get_one_role_listings(listing_id):
    try:
        # Get a single record from the database
        role_listing = RoleListing.query.filter_by(listing_id=listing_id).first()

        if role_listing:
            role_data = role_listing.json()  # Get existing role listing data as JSON

            # Fetch the skills required for this role
            skills_required = get_skills_by_role(role_listing.role_name)

            # Include the skills in the response
            role_data['skills_required'] = skills_required

            role_desc = Role.query.filter_by(role_name=role_listing.role_name).first()
            role_data['role_desc'] = role_desc.role_desc

            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "role_listing": role_data
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There is not such role listing"
            }
        ), 404

    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

####################################################################################################################################

# STAFF: GET ALL ROLE LISTINGS THAT I HAVE NOT APPLIED YET & IS NOT PAST DEADLINE
@staff_blueprint.route('/role_listings/<int:staff_id>', methods=['GET'])
def get_role_listings_not_applied(staff_id):
    try:
        role_listings_query = RoleListing.query
        role_listings = filter_listings_by_staff_and_deadline(role_listings_query, staff_id).all()

        results = []
        
        # For each role listing, get the role skill match and append it to results
        for listing in role_listings:
            role_data = listing.json()
            skill_match_data = role_skill_match(staff_id, listing.role_name)
            
            role_desc = Role.query.filter_by(role_name=listing.role_name).first()
            role_data['role_desc'] = role_desc.role_desc

            # If the role skill match was successful, add it to results
            if skill_match_data.get('code') == 200:
                results.append({
                    "role_listing": role_data,
                    "role_skill_match": skill_match_data['data']
                })

        # If there are records, return the records
        if results:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "role_listings_with_skill_match": results
                    }
                }
            )

        # If not, return 404 - nothing found
        return jsonify(
            {
                "code": 404,
                "message": "There are no role listings"
            }
        ), 404

    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500
        
@staff_blueprint.route('/browse_role_listings/<int:staff_id>/<string:search_input>', methods=['GET'])
def browse_listing(staff_id, search_input):
    try:
        # Check for special characters and numbers
        if not re.match("^[a-zA-Z\s]*$", search_input):
            return jsonify(
                {
                    "code": 400,
                    "message": "Search input contains invalid characters or numbers."
                }
            ), 400

        search_term = "%{}%".format(search_input)
        role_listings_query = RoleListing.query.outerjoin(
            RoleSkill, RoleListing.role_name == RoleSkill.role_name
        ).filter(
            or_(
                RoleListing.role_name.ilike(search_term),
                RoleListing.category.ilike(search_term),
                RoleSkill.skill_name.ilike(search_term)
            )
        )

        role_listings = filter_listings_by_staff_and_deadline(role_listings_query, staff_id).distinct().all()

        results = []
        
        # For each role listing, get the role skill match and append it to results
        for listing in role_listings:
            skill_match_data = role_skill_match(staff_id, listing.role_name)
            roles = Role.query.filter_by(role_name=listing.role_name).first()
            listing = listing.json()
            role_desc = roles.role_desc
            listing["role_desc"] = role_desc
            
            # If the role skill match was successful, add it to results
            if skill_match_data.get('code') == 200:
                results.append({
                    "role_listing": listing,
                    "role_skill_match": skill_match_data['data']
                })

        # If there are records, return the records
        if results:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "role_listings_with_skill_match": results
                    }
                }
            )

        # If not, return 404 - nothing found
        return jsonify(
            {
                "code": 404,
                "message": "There are no role listings matching your query."
            }
        ), 404

    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

# STAFF: VIEW ALL ROLES APPLIED
@staff_blueprint.route('/applied_roles_with_skill_match/<int:staff_id>', methods=['GET'])
def view_applied_roles_with_skill_match(staff_id):
    try:
        # Get all the applications by the staff
        applications = JobApplication.query.filter_by(staff_id=staff_id).all()

        results = []
        for application in applications:
            # Get associated role listing for this application
            role_listing = RoleListing.query.filter_by(listing_id=application.listing_id).first()
            if role_listing:
                # Get skill match for this role
                skill_match_data = role_skill_match(staff_id, role_listing.role_name)
                if skill_match_data['code'] == 200:
                    role_skill_data = skill_match_data['data']
                    role_skill_data = skill_match_data['data']
                    results.append({
                        "role_listing": role_listing.json(),
                        "role_skill_match": role_skill_data
                    })

        if results:
            return jsonify({"code": 200, "data": {"applied_roles_with_skill_match": results}}), 200
        else:
            return jsonify({"code": 404, "message": "No applied roles found for the given staff ID."}), 404

    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500
    

# STAFF: GET ALL FILTER OPTIONS 
@staff_blueprint.route('/filter_options', methods=['GET'])
def get_filter_options():
    try:
        # Get all the categories in the database
        categories = Category.query.all()

        result_category = []
        for category in categories:
            # Check if category is unique
            if category.category not in result_category:
                result_category.append(category.category)

        # Get all the staff in the database
        staffs = Staff.query.all()

        result_dept = []
        for staff in staffs:
            if staff.dept not in result_dept:
                result_dept.append(staff.dept)

        if result_category and result_dept:
            return jsonify({"code": 200, "data": {"department": result_dept, "category": result_category}}), 200
        else:
            return jsonify({"code": 404, "message": "Was no able to retrieve filter options"}), 404

    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500
    

# STAFF: GET THE FILTERED ROLE LISTINGS
@staff_blueprint.route('/filter_role_listings/<int:staff_id>', methods=['GET'])
def get_filtered_roles(staff_id):
    try:

        # Extract data from the request
        data = request.get_json() 
        print("cat ", data["category"])

        all_role_listings = RoleListing.query
        # Get all role listing applicable for the staff
        avaliable_role_listings = filter_listings_by_staff_and_deadline(all_role_listings, staff_id).all()

        # If both category and department are in the filter options
        if len(data['category']) != 0 and len(data["department"]) != 0:
            role_listings_query = []
            # Get the list of department and category from the filter options
            filter_category = data['category']
            filter_department = data['department']

            # For each role listing, check if it has the given department
            for role_listing in avaliable_role_listings:
                if role_listing.department in filter_department:
                    # Check if the role listing has the given category
                    if role_listing.category in filter_category:
                        # Append to the role_listings_query list if it has both
                        role_listings_query.append(role_listing)
        
        # If only category is in the filter option
        elif len(data['category']) != 0 :
            role_listings_query = []
            # Get the list of department and category from the filter options
            filter_category = data['category']

            # For each role listing, check if it has the given category
            for role_listing in avaliable_role_listings:
                if role_listing.category in filter_category:
                    # Append to the role_listings_query list if it has both
                    role_listings_query.append(role_listing)
        
        # If only department is in the filter option
        elif len(data["department"]) != 0:
            role_listings_query = []
            # Get the list of department and category from the filter options
            filter_department = data['department']

            # For each role listing, check if it has the given department
            for role_listing in avaliable_role_listings:
                if role_listing.department in filter_department:
                    # Append to the role_listings_query list if it has both
                    role_listings_query.append(role_listing)        
        else:
            return jsonify({"code": 400, "message": "Invalid filter option."}), 400
        
        print("role_listings_query ", [each.json() for each in role_listings_query])

        results = []
        # If match percentage if in the filter option
        if len(data['match_percentage']) != 0 and len(role_listings_query) != 0:
            # Get the upper and lower bound of the match percentage filter
            bounds = data['match_percentage'].split('-')
            lower_bound = int(bounds[0])
            upper_bound = int(bounds[1])
            print(upper_bound ,"-", lower_bound)

            # For each role listing, get the role skill match and check if its between the match percentage
            for role_listing in role_listings_query:
                print("role listing name ", role_listing.role_name)
                skill_match = role_skill_match(staff_id, role_listing.role_name)
                if skill_match['code'] == 200:
                    match_percentage = int(float(skill_match['data']["match_percentage"]))
                    # Check if match percentage if between the lower and upper bound
                    if match_percentage >= lower_bound and match_percentage <= upper_bound:
                        # Get the role description
                        roles = Role.query.filter_by(role_name=role_listing.role_name).first()
                        role_desc = roles.role_desc
                        listing = role_listing.json()
                        # Add the role description to the role listing
                        listing["role_desc"] = role_desc
                        # Append the role listing information and the skill match information to results
                        results.append({
                            "role_listing": listing,
                            "role_skill_match": skill_match['data']
                        })
        
        # If there are results, return the results, else return that no results were found
        if results:
            return jsonify({"code": 200, "data": {"role_listings": results}}), 200
        else:
            return jsonify({"code": 404, "message": "No role listings found for the given filter options."}), 404

    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500