from . import main, auth

__all__ = ['main_bp', 'auth_bp']

main_bp = main.bp
auth_bp = auth.auth