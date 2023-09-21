from flask import request, jsonify
from database import db
from models.role_listing import RoleListing
from blueprints.hr_blueprint import hr_blueprint
from models.role_skill import RoleSkill 

# Handles the logic where HR creates role listing
@hr_blueprint.route('/create_role_listing', methods=['POST'])
def create_role_listing():
    try:
        # Extract data from the request
        data = request.get_json()

        # Validate that all required keys are present
        required_keys = ['role_name', 'department', 'category', 'deadline']
        if not all(key in data for key in required_keys):
            return jsonify({"error": "Missing required field(s)"}), 400

        # Extract validated fields
        role_name, department, category, deadline = [data[k] for k in required_keys]

        # Query for skills related to the role_name
        skills_result = RoleSkill.query.filter_by(role_name=role_name).all()
        skills_list = [skill.skill_name for skill in skills_result] 

        # Check for duplicate role listing
        existing_role = RoleListing.query.filter_by(
            role_name=role_name,
            department=department,
            category=category,
            deadline=deadline,
        ).first()

        if existing_role:
            return jsonify({"error": "Duplicate role listing"}), 400

        # Create a new role listing object
        new_role_listing = RoleListing(
            role_name=role_name,
            department=department,
            category=category,
            deadline=deadline,
        )

        # Add the new role listing to the database
        db.session.add(new_role_listing)
        db.session.commit()

        return jsonify(
            {
                "code": 201,
                "data": new_role_listing.json(),
                "skills_required": skills_list  # Include the list of skills in the response
            }  
            
        ), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

