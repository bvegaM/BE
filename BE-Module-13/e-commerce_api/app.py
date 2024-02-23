from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from database import db
from caching import cache
from routes.cutomerBluePrint import customer_blueprint
from routes.customerManagementBluePrint import customer_management_blueprint
from models.customer import Customer
from models.customerManagement import CustomerManagement
from models.role import Role
from models.customerManagementRole import CustomerManagementRole
from werkzeug.security import generate_password_hash


limiter = Limiter(key_func=get_remote_address)

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)

    return app


def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customer')
    app.register_blueprint(customer_management_blueprint, url_prefix='/management')

def config_rate_limit():
    limiter.limit("100 per day")(customer_blueprint)

def init_roles_data():
    roles = [
        Role(role_name='admin'),
        Role(role_name='user'),
        Role(role_name='guest')
    ]

    db.session.add_all(roles)
    db.session.commit()

def init_customers_info_data():
    customers = [
        Customer(name="Customer One", email="customer1@exmaple.com",phone_number="092319283"),
        Customer(name="Customer Two", email="customer2@exmaple.com",phone_number="092319283"),
        Customer(name="Customer Three", email="customer3@exmaple.com",phone_number="092319283"),
    ]

    db.session.add_all(customers)
    db.session.commit()
    
    customersManagement = [
        CustomerManagement(username="ctm1", password=generate_password_hash("password1"),customer_id=1),
        CustomerManagement(username="ctm2", password=generate_password_hash("password2"),customer_id=2),
        CustomerManagement(username="ctm3", password=generate_password_hash("password3"),customer_id=3),
    ]
    db.session.add_all(customersManagement)
    db.session.commit()

def init_roles_customers_data():

    roles_customers = [
        CustomerManagementRole(customer_management_id=1, role_id=1),
        CustomerManagementRole(customer_management_id=2, role_id=2),
        CustomerManagementRole(customer_management_id=2, role_id=3)
    ]

    db.session.add_all(roles_customers)
    db.session.commit()


if __name__ == '__main__':
    app = create_app('DevelopmentConfig')
    blue_print_config(app)
    config_rate_limit()

    with app.app_context():
        db.drop_all()
        db.create_all()

        init_roles_data()
        init_customers_info_data()
        init_roles_customers_data()
     
    app.run(debug=True)