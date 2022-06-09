from flask import Flask

app = Flask(__name__)

# devs can return a status code when code executes
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

@app.route('/')
def teapot():
    # this error code returns 'I am a Tea pot'
    # a cute little joke
    return "What is your favorite tea?", 418

if __name__ == '__main__':
    # Runs the Flask app

    # host specifies where the app runs
    # default values are 127.0.0.1 and localhost
    app.run(host='localhost', debug=True)