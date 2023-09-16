from flask import Flask, jsonify
from os import environ
from flask_cors import CORS
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/sbrp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db.init_app(app)
CORS(app)

from models.staff import Staff
from models.role import Role
from models.access_rights import AccessRights

# # Register Blueprints (Adjusted according to your blueprint names)
# from controllers import (role_creation_controller)
# app.register_blueprint(role_creation_controller.bp)
# # app.register_blueprint(role_listing_view_controller.bp)
# # app.register_blueprint(skill_match_controller.bp)
# # app.register_blueprint(staff_view_controller.bp)
# # app.register_blueprint(staff_application_controller.bp)

@app.route('/test_db')
def test_db():
    try:
        # Create new entries and add them to the session
        new_staff = Staff(staff_fname="Test First", staff_lname="Test Last", dept="Test Dept", email="test@example.com", access_rights=1)
        new_role = Role(role_name="Test Role", role_desc="This is a test role")
        new_access_right = AccessRights(access_right=1, user_role="Admin")


        db.session.add(new_staff)
        db.session.add(new_role)
        db.session.add(new_access_right)
        db.session.commit()

        # Query the database for all entries
        staff_results = Staff.query.all()
        role_results = Role.query.all()
        access_rights_results = AccessRights.query.all()

        return jsonify(staff=[str(result) for result in staff_results], role=[str(result) for result in role_results], access_rights=[str(result) for result in access_rights_results])
    except Exception as e:
        db.session.rollback()
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode


