# This controller handles the creation of new role listings by HR users.
# It validates input data, checks for duplicate active listings, and saves the new listing.
# Includes helper endpoints to fetch data for dropdowns (roles, skills, descriptions, departments, categories).

from flask import request, jsonify
from database import db
from models.role_listing import RoleListing
from blueprints.hr_blueprint import hr_blueprint
from blueprints.staff_blueprint import staff_blueprint
from models.role_skill import RoleSkill 
from models.role import Role
from models.category import Category
from models.staff import Staff
from datetime import date, datetime

# HR: CREATES A ROLE LISTING
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

        deadline_date = datetime.strptime(deadline, '%Y-%m-%d')
        if datetime.today() > deadline_date:
            return jsonify({"error": "Deadline must be in the future"}), 400 

        # Check for existing role listing with same role name, category, and department
        existing_role = RoleListing.query.filter_by(
            role_name=role_name,
            department=department,
            category=category
        ).first()

        # Check if the deadline for the existing role has passed
        if existing_role:
            if isinstance(existing_role.deadline, str):
                existing_role_deadline = datetime.strptime(existing_role.deadline, '%Y-%m-%d').date()
            else:
                existing_role_deadline = existing_role.deadline

            if datetime.today().date() <= existing_role_deadline:
                return jsonify({"error": "A role listing with the same details exists and its deadline has not passed yet."}), 400
                
        # Create a new role listing object
        new_role_listing = RoleListing(
            role_name=role_name,
            department=department,
            category=category,
            deadline=deadline_date,
        )

        # Add the new role listing to the database
        db.session.add(new_role_listing)
        db.session.commit()

        return jsonify(
            {
                "code": 201,
                "data": new_role_listing.json(),
            }  
        ), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

# GET SKILLS REQUIRED FOR A SPECIFIC ROLE
@hr_blueprint.route('/get_role_skills/<string:role_name>', methods=['GET'])
def get_role_skills(role_name):
    try:
        skills_result = RoleSkill.query.filter_by(role_name=role_name).all()
        skills_list = [skill.skill_name for skill in skills_result]
        return jsonify({"skills_required": skills_list}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET ALL ROLE NAMES
@hr_blueprint.route('/get_role_names', methods=['GET'])
def get_role_names():
    try:
        roles = Role.query.all()
        return jsonify([role.role_name for role in roles]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET DESCRIPTION FOR SPECIFIC ROLE
@hr_blueprint.route('/role/<string:role_name>/description', methods=['GET'])
def get_role_description(role_name):
    try:
        role = Role.query.filter_by(role_name=role_name).first()
        desc = role.role_desc
        paragraphs_list = desc.split('<br>')
        return jsonify(description=paragraphs_list), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# GET DEPARTMENTS FROM STAFF TABLE
@hr_blueprint.route('/departments', methods=['GET'])
def get_departments():
    try:
        staffs = Staff.query.all()
        
        departments = []
        for staff in staffs:
            if staff.dept not in departments:
                departments.append(staff.dept)
        return jsonify(departments), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# GET ALL CATEGORY NAMES
@hr_blueprint.route('/categories', methods=['GET'])
def get_category_names():
    try:
        categories = Category.query.all()
        return jsonify([category.category for category in categories]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    