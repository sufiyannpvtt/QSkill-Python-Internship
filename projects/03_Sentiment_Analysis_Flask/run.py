from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.routes import main

def create_app():
    app = Flask(
        __name__,
        template_folder="app/templates",
        static_folder="app/static"
    )

    Limiter(
        get_remote_address,
        app=app,
        default_limits=["100 per hour"]
    )

    app.register_blueprint(main)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)
