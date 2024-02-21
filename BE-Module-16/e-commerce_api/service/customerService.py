from models.customer import Customer
from circuitbreaker import circuit
from database import db

def fallback_function(customer):
    return "Circuit Braker activate"

@circuit(failure_threshold=2,  recovery_timeout=10, fallback_function=fallback_function)
def save_customer(customer):
    customer_save = Customer(customer['name'], customer['email'], customer['phone'])
    db.session.add(customer_save)
    db.session.commit()
    db.session.refresh(customer_save)
    return customer_save.serialize()

def find_all_customer():
    customers = Customer.query.all()
    return [customer.serialize() for customer in customers]

def find_customer_by_id(customer_id):
    customer = Customer.query.filter(Customer.id == customer_id).one_or_none()
    if customer is None:
        return None
    return customer.serialize()