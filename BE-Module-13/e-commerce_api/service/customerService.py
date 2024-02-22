from models.customer import Customer
from circuitbreaker import circuit
from database import db
from models.customerManagement import CustomerManagement

def fallback_function(customer):
    return "Circuit Braker activate"

@circuit(failure_threshold=2,  recovery_timeout=10, fallback_function=fallback_function)
def save_customer(customer):
    try:
        # Start a new transaction
        with db.session.begin_nested() as customer_nested:
            customer_save = Customer(name=customer['name'], email=customer['email'], phone_number=customer['phone'])
            db.session.add(customer_save)

        with db.session.begin_nested() as management_nested:
            # If an error occurs here, the transaction will be rolled back to the savepoint
            customer_management = CustomerManagement(username=customer['management']['username'], password=customer['management']['password'], customer_id=customer_save.id)
            db.session.add(customer_management)
        
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    
    return customer_save.serialize()

def find_all_customer():
    customers = Customer.query.all()
    return [c.serialize() for c in customers]


def find_all__customers_by_pagination(page, per_page):
    customers = Customer.query.paginate(page=page, per_page=per_page)
    return [c.serialize() for c in customers.items]

def find_customer_by_id(customer_id):
    customer = Customer.query.filter(Customer.id == customer_id).one_or_none()
    if customer is None:
        return None
    return customer.serialize()