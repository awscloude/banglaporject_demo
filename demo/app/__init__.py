from flask import Flask
from .routes import routes, login_manager, bcrypt
from .database import db
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

