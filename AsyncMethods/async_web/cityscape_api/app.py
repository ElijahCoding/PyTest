import flask

app = flask.Flask(__name__)
is_debug = True

def run_web_app():
    app.run(debug=is_debug, port=5001)

if __name__ == '__main__':
    run_web_app()