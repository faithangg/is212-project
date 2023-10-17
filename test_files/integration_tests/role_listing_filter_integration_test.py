import unittest
import flask_testing
import json
from app import app, db, Doctor, Patient


class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://" # In-memory database
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {} 
    app.config['TESTING'] = True # Disable error catching during request handling

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCreateConsultation(TestApp):
    def test_create_consultation(self):
        pass


if __name__ == '__main__':
    unittest.main()
