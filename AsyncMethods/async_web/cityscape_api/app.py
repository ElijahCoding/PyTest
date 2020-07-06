import flask
from config import settings

app = flask.Flask(__name__)
is_debug = True

def configure_app():
    mode = 'dev' if is_debug else 'prod'
    data = settings.load(mode)

    print("Using cached data? {}".format(data.get('use_cached_data')))

def run_web_app():
    app.run(debug=is_debug, port=5001)

configure_app()

if __name__ == '__main__':
    run_web_app()