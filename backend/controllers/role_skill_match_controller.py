from flask import request, jsonify
from database import db
from models.role_skill import RoleSkill
from models.staff_skill import StaffSkill
from blueprints.staff_blueprint import staff_blueprint

# Handles the logic where HR creates role listing
@staff_blueprint.route('/role_skill/<string:staff_id>/<string:role_name>', methods=['GET'])
def role_skill_match(staff_id, role_name):
    
    try:
        # Get all the skills based on the roles
        role_skills_db = RoleSkill.query.filter_by(role_name=role_name).all()

        # Get all the skills that the staff has
        staff_skills_db = StaffSkill.query.filter_by(staff_id=staff_id).all()

        # Store all the staff skills in an array
        staff_skills = []

        for skill in staff_skills_db:
            staff_skills.append(skill.skill_name)


        # Loop through and check which skills that staff and lack
        staff_have = []
        staff_dont = []

        for role_skill in role_skills_db:
            current = role_skill.skill_name
            if current in staff_skills:
                staff_have.append(current)
            else:
                staff_dont.append(current)

        # Get the percentage of roles matched -- ???
        match_percentage = (len(staff_have) / (len(staff_have) + len(staff_dont))) * 100

        return jsonify(
                {
                    "code": 200,
                    "data": {
                        "have": [have for have in staff_have],
                        "dont": [dont for dont in staff_dont],
                        "match percentage": match_percentage
                    }
                }
            )
    
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

