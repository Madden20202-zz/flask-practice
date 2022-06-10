from flask import Flask
from contacts import contacts_bp
from home_page import home_bp

app = Flask(__name__)

# the url is localhost:5000/home but /home/hello works as well
app.register_blueprint(home_bp, url_prefix='/home')

app.register_blueprint(contacts_bp, url_prefix='/contacts')

# no if required 
app.run(host='localhost', debug=True)