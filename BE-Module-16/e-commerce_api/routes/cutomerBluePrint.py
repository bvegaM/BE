from flask import Blueprint
from controller.customerController import save, find_all, get_customer_by_id

customer_blueprint = Blueprint('blueprint', __name__)

customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/id/<int:id>', methods=['GET'])(get_customer_by_id)