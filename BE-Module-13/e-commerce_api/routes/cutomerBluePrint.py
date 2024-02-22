from flask import Blueprint
from controller.customerController import find_all_by_pagination, save, find_all, get_customer_by_id


customer_blueprint = Blueprint('customer_bp', __name__)


customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/paginate', methods=['GET'])(find_all_by_pagination)

