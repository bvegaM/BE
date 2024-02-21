import time
from flask import jsonify, request
from caching import cache
from service.customerService import save_customer, find_all_customer, find_customer_by_id

def save():
    customer = request.json
    return save_customer(customer), 201

@cache.cached(timeout=60)
def find_all():
    return find_all_customer(), 200

@cache.memoize(timeout=60)
def get_customer_by_id(id):
    if id is None:
        return jsonify({'error': 'Customer ID is required'}), 400

    customer = find_customer_by_id(id)
    if customer is None:
        return jsonify({'error': 'Customer not found'}), 404

    return customer, 200