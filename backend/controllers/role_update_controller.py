# This controller handles the updating of existing role listings by HR users.
# It allows modification of details like role name, department, category, and deadline,
# ensuring data validity and preventing duplicate entries.

from flask import request, jsonify
from database import db
from models.role_listing import RoleListing
from blueprints.hr_blueprint import hr_blueprint
from datetime import datetime

# HR: UPDATES A ROLE LISTING
@hr_blueprint.route('/update_role_listing/<int:listing_id>', methods=['PUT'])
def update_role_listing(listing_id):
    try:
        # Fetch the role listing to be updated
        existing_role_listing = RoleListing.query.filter_by(listing_id=listing_id).first()

        # Check if the role listing exists
        if not existing_role_listing:
            return jsonify({"error": "Role listing not found"}), 404

        # Extract data from the request
        data = request.get_json()

        # Store original values before update
        original_role_name = existing_role_listing.role_name
        original_department = existing_role_listing.department
        original_category = existing_role_listing.category

        # Update the provided fields if they differ from the original
        if 'role_name' in data and data['role_name'] != existing_role_listing.role_name:
            existing_role_listing.role_name = data['role_name']
        if 'department' in data and data['department'] != existing_role_listing.department:
            existing_role_listing.department = data['department']
        if 'category' in data and data['category'] != existing_role_listing.category:
            existing_role_listing.category = data['category']
        if 'deadline' in data and data['deadline'] != str(existing_role_listing.deadline):
            deadline_date = datetime.strptime(data['deadline'], '%Y-%m-%d')
            if datetime.today() > deadline_date:
                return jsonify({"error": "Deadline must be in the future"}), 400
            existing_role_listing.deadline = data['deadline']

        # Check for duplicate role listing after update
        duplicate_role = RoleListing.query.filter(
            RoleListing.role_name == existing_role_listing.role_name,
            RoleListing.department == existing_role_listing.department,
            RoleListing.category == existing_role_listing.category,
            RoleListing.listing_id != listing_id  # Exclude the current listing from the query
        ).first()

        if duplicate_role:
            # Reset to the original values to avoid unwanted changes in the database
            existing_role_listing.role_name = original_role_name
            existing_role_listing.department = original_department
            existing_role_listing.category = original_category

            return jsonify({"error": "Duplicate role listing after update"}), 400

        # Commit the changes to the database
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "message": "Successfully updated role listing!",
                "data": existing_role_listing.json(),
            }
        ), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while updating the role listing.", "details": str(e)}), 500
