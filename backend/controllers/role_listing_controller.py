from flask import request, jsonify
from database import db
from models.role_listing import RoleListing
from blueprints.hr_blueprint import hr_blueprint

# Handles the logic where HR creates role listing
@hr_blueprint.route('/role_listings', methods=['GET'])
def role_listings():
    
    try:
        # Get all the records from the database
        role_listings = RoleListing.query.all()
        
        # If have records return the records
        if len(role_listings):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "role_listing": [listing.json() for listing in role_listings]
                    }
                }
            )
        
        # If not return 404 - nothing found
        return jsonify(
            {
                "code": 404,
                "message": "There are no role listings"
            }
        ), 404

        
        
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

@hr_blueprint.route('/role_listings/<string:listing_id>', methods=['GET'])
def get_one_role_listings(listing_id):
    try:
        # Get a single record from the database
        role_listing = RoleListing.query.filter_by(listing_id=listing_id).first()
        
        if role_listing:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "role_listing": role_listing.json()
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There is not such role listing"
            }
        ), 404

        
        
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

