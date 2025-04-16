from flask import Blueprint
from flask_login import LoginManager
from app import app


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

login_manager = LoginManager(app)
login_manager.login_view = 'admin.login'



