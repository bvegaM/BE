import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import MovieModel

class Movie(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel

class Query(graphene.ObjectType):
    movies = graphene.List(Movie)

    def resolve_movies(self, info):
        return MovieModel.query.all()