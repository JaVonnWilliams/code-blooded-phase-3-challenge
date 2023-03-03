
from classes.Movie import Movie
from .Review import Review

class Viewer:
    def __init__(self, username):
        self.username = username
        self.reviews = []

    def rate_movie(self, movie, rating):
        review = Review(movie=movie, viewer=self, rating=rating)
        self.reviews.append(review)
        movie.add_review(review)

    def reviewed_movies(self):
        return list(set([review.movie for review in self.reviews]))


# from .Review import Review





    # username property goes here!

    # def reviews(self):
    #     pass

    # def reviewed_movies(self):
    #     pass

    # def movie_reviewed(self, movie):
    #     pass

    # def rate_movie(self, movie, rating):
    #     pass
