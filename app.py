from flask import Flask

app = Flask(__name__)

# Now apps will always redirect when something
# is done, a login page is the best example of this

# When something has a / at the end, 
# the app will read it as a sort of directory,
# where it can be added to
# ex /home/posts
@app.route('/home/')

def home_page():
    return "This is the Home Page"

# This will not be able to move forward,
# and will be a single page app
@app.route('/contact')

def contact_page():
    return "Contacts would come up here"

if __name__ == '__main__':
    # Runs the Flask app

    # host specifies where the app runs
    # default values are 127.0.0.1 and localhost
    app.run(host='localhost', debug=True)