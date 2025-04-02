from flask import request, flash, redirect, url_for, render_template
from flask_login import login_user, login_required, logout_user
from flask import Blueprint
from sqlalchemy import text
from config import config
from ..connection import engine
from ..user import User
from .. import login_manager

cfg = config['current']
auth = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    with engine.connect() as connection:
        result = connection.execute(text(f"select * from {cfg.DB_TABLE} where id='{user_id}'"))
        user_info = result.fetchone()
        user = User(*user_info)
    return user

@auth.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
        flash('Invalid input.')
        return 'not username or not password'
    with engine.connect() as connection:
        result = connection.execute(text(f"select * from {cfg.DB_TABLE} where username='{username}'"))
        user_info = result.fetchone()
        user = User(*user_info)
        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('Login success.')
            return 'success'
        flash('Invalid username or password.')
        return 'Invalid username or password'


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye.')
    return 'Goodbye.'