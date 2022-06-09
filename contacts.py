from flask import Blueprint
from flask import jsonify

# What does Blueprint really do?
# sinply, they allow the dev to create
# various endpoints into their own subdomains

home_bp = Blueprint('home', __name__)
contacts_bp = Blueprint('contacts', __name__)

@home_bp.route('/home/')
def greeting():
    return "Welcome to the Home Page"

@contacts_bp.route('/home/')
def contact_list():
    return "These are your Contacts:"
    return jsonify({
        "Austin": 876,
        "Jeremy": 309,
        "Kyle": 673
    })