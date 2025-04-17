from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlmodel import Session, select
from ..models.user import User
from .. import db, login_manager

auth_bp = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    with Session(db.engine) as session:
        return session.get(User, int(user_id))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        with Session(db.engine) as session:
            user = session.exec(select(User).where(User.username == username)).first()
            
            if user and check_password_hash(user.password_hash, password):
                login_user(user)
                return redirect(url_for('main.index'))
            
            flash('Invalid username or password', 'error')
    
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/change-language/<lang>')
@login_required
def change_language(lang):
    if lang in current_app.config['BABEL_SUPPORTED_LOCALES']:
        current_user.preferred_language = lang
        with Session(db.engine) as session:
            session.add(current_user)
            session.commit()
    return redirect(request.referrer or url_for('main.index')) 