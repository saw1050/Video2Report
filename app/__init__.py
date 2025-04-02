from flask import Flask
from config import config
from flask_login import LoginManager
from pathlib import Path
from flask_cors import CORS

__all__ = ['app', 'socketio']

Path(config['current'].DATA_DUMP_PATH).mkdir(parents=True, exist_ok=True)

app = Flask(__name__)
app.config.from_object(config['current'])
CORS(app, supports_credentials=True) 
login_manager = LoginManager(app)

from . import routes
app.register_blueprint(routes.main_bp)
app.register_blueprint(routes.auth_bp, url_prefix='/auth')



