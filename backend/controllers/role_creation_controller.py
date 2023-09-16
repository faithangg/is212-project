from flask import Blueprint, request, jsonify
from database import db
from models.role_listing import RoleListing

role_creation_bp = Blueprint('role_creation', __name__)

# Handles the logic where HR creates role listing
@role_creation_bp.route('/create_role_listing', methods=['POST'])
def create_role_listing():
    try:
        # Extract data from the request
        data = request.get_json()
        role_name = data['role_name']
        department = data['department']
        category = data['category']
        deadline = data['deadline']

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

        return jsonify(message="Role listing created successfully"), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

