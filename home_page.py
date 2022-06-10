from flask import Blueprint

# What does Blueprint really do?
# sinply, they allow the dev to create
# various endpoints into their own subdomains

home_bp = Blueprint('home', __name__)

@home_bp.route('/home/')
def greeting():
    return "Welcome to the Home Page"
