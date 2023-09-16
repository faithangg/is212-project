from flask import Flask, jsonify
from os import environ
from flask_cors import CORS
from database import db
from controllers.role_creation_controller import role_creation_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/sbrp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db.init_app(app)
CORS(app)

app.register_blueprint(role_creation_bp)

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode


