from flask import jsonify, request
from flask_jwt_extended import jwt_required
from caching import cache
from service.customerService import save_customer, find_all_customer, find_customer_by_id, find_all__customers_by_pagination
from utils.util import role_required, token_required

def save():
    customer = request.json
    return save_customer(customer), 201

@token_required
@role_required('admin')
def find_all(token):
    return find_all_customer(), 200

def find_all_by_pagination():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return find_all__customers_by_pagination(page=page, per_page=per_page), 200

@cache.memoize(timeout=60)
def get_customer_by_id(id):
    if id is None:
        return jsonify({'error': 'Customer ID is required'}), 400

    customer = find_customer_by_id(id)
    if customer is None:
        return jsonify({'error': 'Customer not found'}), 404

    return customer, 200