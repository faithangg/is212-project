from flask import request, jsonify
from database import db
from sqlalchemy import or_
from models.role_listing import RoleListing
from models.role import Role 
from models.category import Category
from models.staff import Staff
from blueprints.hr_blueprint import hr_blueprint
from models.staff_skill import StaffSkill
from models.role_skill import RoleSkill 
from models.job_application import JobApplication

# HELPER FUNCTION TO GET ROLE SKILL MATCH
def role_skill_match(staff_id, role_name):
    try:
        # Get all the skills based on the roles
        role_skills = [rs.skill_name for rs in RoleSkill.query.filter_by(role_name=role_name).all()]

        # Get all the skills that the staff has
        staff_skills = [ss.skill_name for ss in StaffSkill.query.filter_by(staff_id=staff_id).all()]

        # Determine skills that staff have and don't have based on the role's requirements
        staff_have = [skill for skill in role_skills if skill in staff_skills]
        staff_dont = [skill for skill in role_skills if skill not in staff_skills]

        # Calculate the percentage of roles matched
        if len(staff_have) + len(staff_dont) == 0:
            match_percentage = 0
        else:
            match_percentage = round((len(staff_have) / (len(staff_have) + len(staff_dont))) * 100)

        return {
            "code": 200,
            "data": {
                "have": staff_have,
                "dont": staff_dont,
                "match_percentage": str(match_percentage)
            }
        }
    except Exception as e:
        # Return an error in a dictionary format
        return {
            "code": 500,
            "error": str(e)
        }

# HELPER FUNCTION TO GET THE SKILL MATCH TO RETURN BACK TO FRONTEND
def get_results(applicants):
    results = []

    # For each application, get the role skill match and check if its between the match percentage
    for application in applicants:
        skill_match = role_skill_match(application["staff_id"], application["role_name"])
        # If the skill match is successful
        if skill_match['code'] == 200:
            # Add the skills they have, dont and the match percentage to the applicant information
            application["skills_dont"] = skill_match['data']["dont"]
            application["skills_have"] = skill_match['data']["have"]
            application["match_percentage"] = skill_match['data']["match_percentage"]
            # Append the application information to results
            results.append(application)
    return results

# HELPER FUNCTION TO GET THE APPLICANTS THAT MEET THE DEPT FILTERS
def get_dept_filtered_applicants(dept_filters, applicants):
    results = []
    # For each application, check if it has the given department
    for application in applicants:
        if application["department"] in dept_filters:
            # Append to the results list if it has both
            results.append(application)

    return results

# HELPER FUNCTION TO GET APPLICANTS WITHIN THE MATCH PERCENTAGE RANGE
def get_match_percentage_filtered_applicants(applicants, match_percentage):
        results = []
        # Get the upper and lower bound of the match percentage filter
        bounds = match_percentage.split('-')
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1])

        # For each application, get the role skill match and check if its between the match percentage
        for application in applicants:
            skill_match = role_skill_match(application["staff_id"], application["role_name"])
            # If the skill match is successful
            if skill_match['code'] == 200:
                match_percentage = int(float(skill_match['data']["match_percentage"]))
                # Check if match percentage if between the lower and upper bound
                if match_percentage >= lower_bound and match_percentage <= upper_bound:
                    # Append the application to results if its between the bounds
                    results.append(application)
        return results

# HELPER FUNCTION TO PLACE THE APPLICATION INFORMATION, STAFF INFORMATION AND LISTING INFORMATION IN ON JSON 
def get_applicant_data(applications):
    applicant_data = []
    for application, staff, listing in applications:
        applicant_data.append({
            "staff_id": staff.staff_id,
            "name": f"{staff.staff_fname} {staff.staff_lname}",
            "email": staff.email,
            "department": staff.dept,  
            "application_date": application.application_date.strftime('%Y-%m-%d'),
            "listing_id": application.listing_id,
            "role_name": listing.role_name
        })
    return applicant_data

####################################################################################################################################

# HR: GET ALL FILTER OPTIONS 
@hr_blueprint.route('/filter_options', methods=['GET'])
def get_filter_options():
    try:
        # Get all the staff in the database
        staffs = Staff.query.all()

        result_dept = []
        for staff in staffs:
            if staff.dept not in result_dept:
                result_dept.append(staff.dept)

        if result_dept:
            return jsonify({"code": 200, "data": {"department": result_dept}}), 200
        else:
            return jsonify({"code": 404, "message": "Was no able to retrieve filter options"}), 404

    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500
        

@hr_blueprint.route('/filter_applicants/<int:listing_id>', methods=['GET', 'POST'])
def get_filtered_roles(listing_id):
    try:
        # Extract data from the request
        data = request.get_json() 

        # Get the filter options chosen for department and match percentage
        department_filters = data['department']
        match_percentage_filters = data['match_percentage']

        # Extract the sort_by parameter from the request
        sort_by = data.get('sort_by', 'newest')

        # Get all applicants for the role listing
        all_applicants = db.session.query(JobApplication, Staff, RoleListing).join(
            Staff, JobApplication.staff_id == Staff.staff_id
        ).filter(
            JobApplication.listing_id == listing_id
        ).filter(
            RoleListing.listing_id == listing_id
        ).all()

        # Get the applicant information
        applicant_info = get_applicant_data(all_applicants)


        applicant_query = []

        # If both department and match percentage are in the filter option
        if len(department_filters) != 0 and len(match_percentage_filters) != 0:
            dept_result = get_dept_filtered_applicants(department_filters, applicant_info)
            for match_percentage in match_percentage_filters:
                match_result = get_match_percentage_filtered_applicants(dept_result, match_percentage)
                if match_result:
                    for applicant in match_result:
                        applicant_query.append(applicant)

            print(applicant_query)

        # If only department is in the filter option
        elif len(department_filters) != 0:
            applicant_query = get_dept_filtered_applicants(department_filters, applicant_info)

        # If only match percentage is in the filter option
        elif len(match_percentage_filters) != 0:
            for match_percentage in match_percentage_filters:
                match_result = get_match_percentage_filtered_applicants(applicant_info, match_percentage)
                if match_result:
                    for applicant in match_result:
                        applicant_query.append(applicant)
        # Else it means no filter options where chosen
        else:
            # Return that no filter options were chosen
            return jsonify({"code": 404, "message": "No filter options were chosen."}), 404

        # Get the enriched applicant data.
        results = get_results(applicant_query)

        # Sorting Logic for results
        if sort_by == 'match_asc':
            results.sort(key=lambda x: float(x["match_percentage"])) 
        elif sort_by == 'match_desc':
            results.sort(key=lambda x: float(x["match_percentage"]), reverse=True)
        elif sort_by == 'newest':
            results.sort(key=lambda x: x["application_date"], reverse=True)

        # If there are applicants that meet the chosen filter options
        if results:
            # Return the result
            return jsonify({"code": 200, "data": {"applicants": results}}), 200
        # Else return that no applicants were found
        else:
            return jsonify({"code": 404, "message": "No applicants found for the given filter options."}), 404

    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500