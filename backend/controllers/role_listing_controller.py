from flask import request, jsonify
from database import db
from models.role_listing import RoleListing
from models.role_skill import RoleSkill 
from models.job_application import JobApplication
from blueprints.hr_blueprint import hr_blueprint
from blueprints.staff_blueprint import staff_blueprint

# Helper function to get skills by role_name
def get_skills_by_role(role_name):
    try:
        skills_result = RoleSkill.query.filter_by(role_name=role_name).all()
        skills_list = [skill.skill_name for skill in skills_result]
        return skills_list
    except Exception as e:
        return []

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

# STAFF: GET ALL ROLE LISTINGS THAT I HAVE NOT APPLIED YET
@staff_blueprint.route('/role_listings/<int:staff_id>', methods=['GET'])
def get_role_listings_not_applied(staff_id):
        try:
            # Get listing_ids the staff has applied for
            applied_listings = [application.listing_id for application in JobApplication.query.filter_by(staff_id=staff_id).all()]

            # Fetch the role listings that the staff hasn't applied for
            role_listings = RoleListing.query.filter(~RoleListing.listing_id.in_(applied_listings)).all()

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

