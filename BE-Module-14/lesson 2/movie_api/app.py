from flask import Flask
from flask_graphql import GraphQLView
import graphene
from models import Base, db_session
from schema import Query

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://example_user:example_password@localhost:3306/example_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear las tablas en la base de datos si aún no existen
Base.metadata.create_all(bind=db_session.bind)

schema = graphene.Schema(query=Query)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(debug=True)
