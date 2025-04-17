import os
from pathlib import Path

class DevelopmentConfig:
    # Flask configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    DEBUG = True
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        f"sqlite:///{Path(__file__).parent.parent / 'instance' / 'sales_purchasing.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Babel configuration
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_SUPPORTED_LOCALES = ['en', 'zh_Hant', 'zh_Hans']
    
    # File upload configuration
    UPLOAD_FOLDER = Path(__file__).parent.parent / 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Session configuration
    SESSION_COOKIE_SECURE = False
    REMEMBER_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True 