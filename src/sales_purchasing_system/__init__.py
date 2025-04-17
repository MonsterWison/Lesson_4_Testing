from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babel import Babel
from sqlmodel import SQLModel
from typing import Optional
import os

db = SQLAlchemy()
login_manager = LoginManager()
babel = Babel()

def create_app(config: Optional[str] = None) -> Flask:
    app = Flask(__name__)
    
    # Load configuration
    if config is None:
        config = os.getenv('FLASK_CONFIG', 'development')
    app.config.from_object(f'config.{config.capitalize()}Config')
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    babel.init_app(app)
    
    # Register blueprints
    from .auth import auth_bp
    from .basic_info import basic_info_bp
    from .sales import sales_bp
    from .purchases import purchases_bp
    from .inventory import inventory_bp
    from .accounting import accounting_bp
    from .admin import admin_bp
    from .reports import reports_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(basic_info_bp)
    app.register_blueprint(sales_bp)
    app.register_blueprint(purchases_bp)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(accounting_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(reports_bp)
    
    # Create database tables
    with app.app_context():
        SQLModel.metadata.create_all(db.engine)
    
    return app 