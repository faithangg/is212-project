from flask import request, jsonify
from database import db
from models.role_listing import RoleListing
from models.role import Role 
from models.job_application import JobApplication
from models.staff import Staff
from blueprints.staff_blueprint import staff_blueprint
from .role_listing_controller import role_skill_match

# STAFF: VIEW PROFILE
@staff_blueprint.route('/profile/<int:staff_id>', methods=['GET'])
def view_applied_roles(staff_id):
    try:
        # Get all the applications by the staff
        applications = JobApplication.query.filter_by(staff_id=staff_id).all()

        # Get the details of the staff
        staff = Staff.query.filter_by(staff_id=staff_id).first()

        roles_applied = []
        for application in applications:
            # Get associated role listing for this application
            role_listing = RoleListing.query.filter_by(listing_id=application.listing_id).first()
            if role_listing:
                # Get skill match for this role
                response = role_skill_match(staff_id, role_listing.role_name)
                if response["code"] == 200:  # Note: I changed `response.status_code` to `response["code"]` based on your previous code
                    role_skill_data = response['data']
                    roles_applied.append({
                        "role_listing": role_listing.json(),
                        "role_skill_match": role_skill_data
                    })

        if roles_applied:
            return jsonify({
                "code": 200, 
                "data": {
                    "staff_details": staff.json(),
                    "applied_roles": roles_applied
                }
            }), 200
        else:
            return jsonify({"code": 404, "message": "No applied roles found for the given staff ID."}), 404

    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500
