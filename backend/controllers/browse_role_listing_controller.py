# This controller provides functionality for HR users to browse/search all role listings.
# It allows searching by role name, category, or required skill.
# Used primarily for the HR management interface to view all listings regardless of status.

from flask import jsonify
from database import db
from sqlalchemy import or_
import re
from models.role_listing import RoleListing
from models.role_skill import RoleSkill 
from models.role import Role 
from blueprints.hr_blueprint import hr_blueprint

# HR BROWSE ROLE LISTINGS IN MANAGE ROLE LISTING PAGE
@hr_blueprint.route('/browse_role_listings/<string:search_input>', methods=['GET'])
def hr_browse_listing(search_input):
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
        ).distinct().all()

        results = []
        
        # For each role listing append it to results
        for listing in role_listings_query:
            roles = Role.query.filter_by(role_name=listing.role_name).first()
            listing_data = listing.json()

            # Query for skills associated with the role and append to skills_required
            skills_query = RoleSkill.query.filter_by(role_name=listing.role_name).all()
            skills_required = [skill.skill_name for skill in skills_query]
            listing_data["skills_required"] = skills_required
            
            role_desc = roles.role_desc
            paragraphs_list = role_desc.split('<br>')
            listing_data["role_desc"] = paragraphs_list

            results.append(listing_data)

        # If there are records, return the records
        if results:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "role_listings": results
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
