from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

__all__ = ['User']

class User(UserMixin):
    
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)