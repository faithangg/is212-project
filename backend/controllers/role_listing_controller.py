from flask import request, jsonify
from database import db
from datetime import datetime
from sqlalchemy import or_
import re
from models.role_listing import RoleListing
from models.role_skill import RoleSkill 
from models.job_application import JobApplication
from blueprints.hr_blueprint import hr_blueprint
from blueprints.staff_blueprint import staff_blueprint

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

####################################################################################################################################

# HR: GET ALL ROLE LISTINGS
@hr_blueprint.route('/role_listings', methods=['GET'])
def get_all_role_listings():
    
    try:
        # Get all the records from the database
        role_listings = RoleListing.query.all()
        
        # If have records return the records
        if len(role_listings):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "role_listing": [listing.json() for listing in role_listings]
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

        # If there are records, return the records
        if role_listings:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "role_listing": [listing.json() for listing in role_listings]
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

# STAFF: SEARCH ROLE LISTING IN SEARCH BAR
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

        # If there are records, return the records
        if role_listings:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "role_listing": [listing.json() for listing in role_listings]
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



