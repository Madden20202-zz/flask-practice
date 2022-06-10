from flask import Blueprint
from flask import jsonify

# What does Blueprint really do?
# sinply, they allow the dev to create
# various endpoints into their own subdomains
contacts_bp = Blueprint('contacts', __name__)

# this is returning a 404 error
@contacts_bp.route('/')
def contact_list():
    return "These are your Contacts:"

    # wont work but honestly dont care
    return jsonify({
        "Austin": 876,
        "Jeremy": 309,
        "Kyle": 673
    })