from flask import Flask, jsonify
from os import environ
from flask_cors import CORS
from database import db
import platform

from blueprints.hr_blueprint import hr_blueprint
from blueprints.staff_blueprint import staff_blueprint
import controllers.role_creation_controller # This line ensures that your route functions get registered
import controllers.login_details_controller
import controllers.role_listing_controller
import controllers.job_application_controller
import controllers.role_update_controller
import controllers.view_applicants_controller
import controllers.role_listing_filter_controller
import controllers.staff_profile_controller
import controllers.role_applicant_filter_controller
import controllers.browse_role_listing_controller

def get_db_url():
    system = platform.system()
    if system == "Windows":
        return "mysql+mysqlconnector://root:root@localhost:3306/sbrp"
    else:
        return "mysql+mysqlconnector://root@localhost:3306/sbrp"


app = Flask(__name__)
if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or get_db_url()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"

db.init_app(app)
CORS(app)

app.register_blueprint(hr_blueprint, url_prefix='/hr')
app.register_blueprint(staff_blueprint, url_prefix='/staff')

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode



