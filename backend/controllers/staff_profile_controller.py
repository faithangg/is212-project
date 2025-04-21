# This controller fetches and displays a staff member's profile information.
# It retrieves staff details, skills, access role, and applied roles with skill match percentages.

from flask import request, jsonify
from database import db
from models.role_listing import RoleListing
from models.job_application import JobApplication
from models.staff import Staff
from models.role import Role
from models.staff_skill import StaffSkill
from models.access_rights import AccessRights
from blueprints.staff_blueprint import staff_blueprint
from .role_listing_controller import role_skill_match

def get_staff_skills(staff_id):
    return [skill.skill_name for skill in StaffSkill.query.filter_by(staff_id=staff_id).all()]

# STAFF: VIEW PROFILE
@staff_blueprint.route('/profile/<int:staff_id>', methods=['GET'])
def view_applied_roles(staff_id):
    try:
        # Get all the applications by the staff
        applications = JobApplication.query.filter_by(staff_id=staff_id).all()

        # Get the details of the staff
        staff = Staff.query.filter_by(staff_id=staff_id).first()
        staff_details = staff.json()

        access_right_desc = AccessRights.query.filter_by(access_id=staff_details["role"]).first().access_control_name

        staff_details["role"] = access_right_desc



        # Get the skills of the staff using the helper function
        staff_skills = get_staff_skills(staff_id)

        applied_roles = []
        for application in applications:
            # Get associated role listing for this application
            role_listing = RoleListing.query.filter_by(listing_id=application.listing_id).first()
            if role_listing:
                # Get the role description using the Role model
                role_desc = Role.query.filter_by(role_name=role_listing.role_name).first().role_desc
                paragraphs_list = role_desc.split('<br>')
                # Get skill match for this role
                response = role_skill_match(staff_id, role_listing.role_name)
                if response["code"] == 200:
                    skill_match_data = response
                    role_skill_data = skill_match_data['data']
                    applied_roles.append({
                        "role_listing": role_listing.json(),
                        "role_description": paragraphs_list,
                        "role_skill_match": role_skill_data
                    })


        if applied_roles:
            data = {
                "staff_details": {
                    "info": staff_details,
                    "skills": staff_skills
                },
                "applied_roles": applied_roles
            }
            return jsonify({"code": 200, "data": data}), 200
        else:
            data = {
                "staff_details": {
                    "info": staff_details,
                    "skills": staff_skills
                },
                "applied_roles": "No applied roles found for the given staff ID."
            }
            return jsonify({"code": 200, "data": data}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500
