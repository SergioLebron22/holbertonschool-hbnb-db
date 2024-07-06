from flask import Blueprint
from src.controllers.authentification import login, protected, admin_data

login_bp = Blueprint("login", __name__, url_prefix="/login")
login_bp.route("/", methods=["POST"])(login)

auth_bp = Blueprint("protected", __name__, url_prefix="/protected")
auth_bp.route("/", methods=["GET"])(protected)

admin_bp = Blueprint("admin", __name__, url_defaults="/admin/data")
admin_bp.route("/", methods=['POST', 'PUT', 'DELETE'])(admin_data)