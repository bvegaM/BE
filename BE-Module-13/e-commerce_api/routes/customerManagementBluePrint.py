from flask import Blueprint
from controller.customerManagementController import login

customer_management_blueprint = Blueprint('management_bp', __name__)

customer_management_blueprint.route('/login', methods=['POST'])(login)