from flask import request, jsonify
from database import db
from models.role_listing import RoleListing
from blueprints.hr_blueprint import hr_blueprint

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
                "data": new_role_listing.json()
            }  
        ), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

