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

class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        director = graphene.String()
        year = graphene.Int()

    movie = graphene.Field(Movie)

    def mutate(self, info, id, title=None, director=None, year=None):
        movie = MovieModel.query.filter_by(id=id).first()
        if not movie:
            raise Exception(f'Movie with id {id} not found')

        if title:
            movie.title = title
        if director:
            movie.director = director
        if year:
            movie.year = year

        db.session.commit()
        return UpdateMovie(movie=movie)
    
class DeleteMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        movie = MovieModel.query.filter_by(id=id).first()
        if not movie:
            raise Exception(f'Movie with id {id} not found')

        db.session.delete(movie)
        db.session.commit()

        return DeleteMovie(ok=True)


class Mutation(graphene.ObjectType):
    create_movie = AddMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()
