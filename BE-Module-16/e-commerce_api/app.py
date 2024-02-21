from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from database import db
from caching import cache
from routes.cutomerBluePrint import customer_blueprint


limiter = Limiter(key_func=get_remote_address)

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)

    return app



def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')

def config_rate_limit():
    limiter.limit("100 per day")(customer_blueprint)


if __name__ == '__main__':
    app = create_app('DevelopmentConfig')
    blue_print_config(app)
    config_rate_limit()

    with app.app_context():
        db.create_all()
    
    migrate = Migrate(app, db)
    app.run(debug=True)