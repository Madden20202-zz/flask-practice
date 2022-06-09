from flask import Flask
# multiple imports from one file
from contacts import contacts_bp, home_bp

app = Flask(__name__)

app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(contacts_bp, url_prefix='/contact')

# simplify the last mess of work, 
# no if required 
app.run(host='localhost', debug=True)