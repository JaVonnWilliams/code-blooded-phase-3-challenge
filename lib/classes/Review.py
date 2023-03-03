# from .Viewer import Viewer
# from .Movie import Movie


class Review:
    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        self.__class__.all.append(self)

    def __repr__(self):
        return f"{self.viewer.username} rated {self.movie.title} {self.rating} stars"

    def __str__(self):
        return self.__repr__()

from .Viewer import Viewer
from .Movie import Movie


    # rating property goes here!

    # viewer property goes here!

    # movie property goes here!
