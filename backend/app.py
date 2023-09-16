from flask import Flask, jsonify
from os import environ
from flask_cors import CORS
from database import db

from blueprints.hr_blueprint import hr_blueprint
import controllers.role_creation_controller # This line ensures that your route functions get registered

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/sbrp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db.init_app(app)
CORS(app)

app.register_blueprint(hr_blueprint, url_prefix='/hr')

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode


