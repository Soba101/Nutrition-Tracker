from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    db.init_app(app)
    
    jwt = JWTManager(app)

    from .routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    with app.app_context():
        db.create_all()
    
    return app
