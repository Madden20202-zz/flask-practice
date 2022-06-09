from flask import Flask

# Let's make a more complex app 
# Increment counting app with a name app within it

app = Flask(__name__)

@app.route('/')
def hello_user(name):
    return "Hello " + name

if __name__ == '__main__':
    # Runs the Flask app

    # host specifies where the app runs
    # default values are 127.0.0.1 and localhost
    app.run(host='localhost', debug=True)