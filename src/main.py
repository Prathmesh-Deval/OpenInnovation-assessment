from flask import Flask


def create_flask_app() -> Flask:
    app = Flask(__name__)
    app.config['CORS_HEADERS'] = 'application/json'
    app.secret_key = b'secret key'

    return app


def init_api(flask_app: Flask) -> Flask:
    from apis import rest_api
    rest_api.init_app(flask_app)
    return flask_app


flask_app = create_flask_app()
flask_app = init_api(flask_app)

if __name__ == "__main__":
    flask_app.run()
