from flask import request, jsonify
from database import db
from models.login_details import LoginDetails
from models.staff import Staff
from blueprints.staff_blueprint import staff_blueprint
import rsa

# Handles the logic where HR creates role listing
@staff_blueprint.route('/login_details', methods=['GET'])
def login_details():
    
    try:
        publicKey, privateKey = rsa.newkeys(512)
        message = "hashed_password_for_john"

        encMessage = rsa.encrypt(message.encode(),publicKey)
        print(encMessage)



        # Extract data from the request
        data = request.get_json()
        staff_id = data['staff_id']
        staff_password = data['staff_password']


        # Get the password from the database
        login = LoginDetails.query.filter_by(staff_id=staff_id).first()
        
        if login:
            db_password_encoded = login.staff_password
            db_password_decoded = login.staff_password

            # print(db_password_decoded)
            if(db_password_decoded != staff_password):
                return jsonify(
                    {
                        "code": 500,
                        "data": "The password or staff id is incorrect"

                    }  
                ), 500
            
            else:
                staff = Staff.query.filter_by(staff_id=staff_id).first()
                return jsonify(
                    {
                        "code": 201,
                        "access_rights": staff.access_rights

                    }  
                ), 201
        


        return jsonify(
            {
                "code": 500,
                "data": "The password or staff id is incorrect"
            }
        ), 500

        
        
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

