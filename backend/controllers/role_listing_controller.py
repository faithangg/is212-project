from flask import request, jsonify
from database import db
from datetime import datetime
from sqlalchemy import or_
import re
from models.role_listing import RoleListing
from models.role_skill import RoleSkill 
from models.role import Role 
from models.job_application import JobApplication
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
        role_skills_db = RoleSkill.query.filter_by(role_name=role_name).all()

        # Get all the skills that the staff has
        staff_skills_db = StaffSkill.query.filter_by(staff_id=staff_id).all()

        # Store all the staff skills in an array
        staff_skills = []

        for skill in staff_skills_db:
            staff_skills.append(skill.skill_name)


        # Loop through and check which skills that staff and lack
        staff_have = []
        staff_dont = []

        for role_skill in role_skills_db:
            current = role_skill.skill_name
            if current in staff_skills:
                staff_have.append(current)
            else:
                staff_dont.append(current)

        # Get the percentage of roles matched -- ???
        match_percentage = (len(staff_have) / (len(staff_have) + len(staff_dont))) * 100

        match_percentage = str(match_percentage)

        return {
                    "code": 200,
                    "data": {
                        "have": [have for have in staff_have],
                        "dont": [dont for dont in staff_dont],
                        "match_percentage": match_percentage
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
            
            # If the role skill match was successful, add it to results
            if skill_match_data.get('code') == 200:
                results.append({
                    "role_listing": listing.json(),
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