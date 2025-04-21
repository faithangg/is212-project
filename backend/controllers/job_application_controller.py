# This controller handles the process of a staff member applying for a role.
# It takes staff_id and listing_id, checks for existing applications by the same staff for the role,
# and creates a new application record if none exists.

from flask import request, jsonify
from database import db
from models.job_application import JobApplication
from blueprints.staff_blueprint import staff_blueprint
from datetime import datetime

# STAFF: APPLY FOR A ROLE
@staff_blueprint.route('/apply_for_role', methods=['POST'])
def apply_for_role():
    try: 
        data = request.get_json()
        staff_id = data['staff_id']
        listing_id = data['listing_id']
        
        # Check if the staff member has already applied for this role
        application = JobApplication.query.filter_by(staff_id=staff_id, listing_id=listing_id).first()
        if application:
            return jsonify(
                    {   
                        "code": 400,
                        "data" : {
                            "message": "You have already applied for this role!"
                        }
                    }
                ), 400
        
        # If not, create a new job application entry
        new_application = JobApplication(staff_id=staff_id, listing_id=listing_id, application_date=datetime.now())
        db.session.add(new_application)
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "data": {
                    "message": "Successfully applied for the role!",
                    "application": new_application.json()
                }
            }
        ), 200

    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500
