from flask import jsonify, request
from database import db
from models.staff import Staff
from models.role_listing import RoleListing
from models.job_application import JobApplication
from blueprints.hr_blueprint import hr_blueprint
from .role_listing_controller import role_skill_match

# HR: VIEW ALL APPLICANTS FOR A PARTICULAR ROLE
@hr_blueprint.route('/role_applicants/<int:listing_id>', methods=['GET'])
def view_role_applicants(listing_id):
    try:
        role_listing = RoleListing.query.get_or_404(listing_id)

        # Fetch applicants for the role listing
        applications = db.session.query(JobApplication, Staff).join(
            Staff, JobApplication.staff_id == Staff.staff_id
        ).filter(
            JobApplication.listing_id == listing_id
        ).all()
        
        if not applications:
            return jsonify({
                "code": 404,
                "message": f"No applicants found for role listing {role_listing.role_name}"
            }), 404

        applicant_data = []

        for application, staff in applications:
            skill_match_data = role_skill_match(staff.staff_id, role_listing.role_name)
            
            if skill_match_data['code'] == 200:
                applicant_data.append({
                    "name": f"{staff.staff_fname} {staff.staff_lname}",
                    "email": staff.email,
                    "department": staff.dept,  
                    "application_date": application.application_date.strftime('%Y-%m-%d'),
                    "match_percentage": skill_match_data['data']['match_percentage'],
                    "skills_have": skill_match_data['data']['have'],
                    "skills_dont": skill_match_data['data']['dont']
                })
            else:
                applicant_data.append({
                    "name": f"{staff.staff_fname} {staff.staff_lname}",
                    "email": staff.email,
                    "department": staff.dept,  
                    "application_date": application.application_date.strftime('%Y-%m-%d'),
                    "match_percentage": "Error",
                    "skills_have": [],
                    "skills_dont": []
                })

        data = {
            "role_name": role_listing.role_name,
            "department": role_listing.department,
            "deadline": role_listing.deadline.strftime('%Y-%m-%d'),
            "total_applicants": len(applicant_data),
            "applicants": applicant_data
        }

        return jsonify({
            "code": 200,
            "data": data
        }), 200
        
    except Exception as e:

        return jsonify({"error": str(e)}), 500

