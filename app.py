from flask import Flask
from flask import jsonify

# Now these last ones were incredibly basic building blocks
# lets add functionality and the ability to communicate
# most information is sent as a JSON output which 
# then can be used in multiple ways, usually to wrap 
# needed information, learn more at
# https://www.w3schools.com/js/js_json_intro.asp

app = Flask(__name__)

@app.route('/')

# this is a basic representation of pre-filled in 
# data being shown. In a more complex example, 
# the data would be taken from a table and then wrapped
def hello_user():
    return jsonify({'name': 'Austin',
                    'role': 'Junior Dev'})

# simultaniously, let's get data that 
# is being counted then shown

@app.route('/numbers')
def print_numbers():
    return jsonify(list(range(5)))

if __name__ == '__main__':
    # Runs the Flask app

    # host specifies where the app runs
    # default values are 127.0.0.1 and localhost
    app.run(host='localhost', debug=True)