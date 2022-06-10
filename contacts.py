from flask import Blueprint
from flask import jsonify

# What does Blueprint really do?
# sinply, they allow the dev to create
# various endpoints into their own subdomains
contacts_bp = Blueprint('contacts', __name__)
@contacts_bp.route('/')
def contact_list():
    return "These are your Contacts:"

    # why would a double return not work
    return jsonify({
        "Austin": 876,
        "Jeremy": 309,
        "Kyle": 673
    })