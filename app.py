from flask import Flask
# multiple imports from one file
from contacts import contacts_bp, home_bp

app = Flask(__name__)



if __name__ == '__main__':
    # Runs the Flask app

    # host specifies where the app runs
    # default values are 127.0.0.1 and localhost
    app.run(host='localhost', debug=True)