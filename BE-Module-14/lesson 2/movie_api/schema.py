# schema.py

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Movie as MovieModel, db

class Movie(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel

class Query(graphene.ObjectType):
    movies = graphene.List(Movie)
    search_movies = graphene.List(Movie, title=graphene.String(), director=graphene.String(), year=graphene.Int())

    def resolve_movies(self, info):
        return MovieModel.query.all()
    
    def resolve_search_movies(self, info, title=None, director=None, year=None):
        query = MovieModel.query
        if title:
            query = query.filter(MovieModel.title.ilike(f'%{title}%'))
        if director:
            query = query.filter(MovieModel.director.ilike(f'%{director}%'))
        if year:
            query = query.filter(MovieModel.year == year)
        return query.all()

class AddMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        director = graphene.String(required=True)
        year = graphene.Int(required=True)

    movie = graphene.Field(Movie)

    def mutate(self, info, title, director, year):
        movie = MovieModel(title=title, director=director, year=year)
        db.session.add(movie)
        db.session.commit()
        return AddMovie(movie=movie)

class Mutation(graphene.ObjectType):
    create_movie = AddMovie.Field()
