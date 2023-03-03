# from .Review import Review



class Movie:
    all = []

    def __init__(self, title):
        self.title = title
        self.reviews_list = []
        self.__class__.all.append(self)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0:
            self.__title = value
        else:
            raise ValueError("Title must be a non-empty string.")

    def reviews(self):
        return self.reviews_list

    def reviewers(self):
        return list(set([review.viewer for review in self.reviews_list]))

    def average_rating(self):
        if len(self.reviews_list) == 0:
            return None
        else:
            total = sum([review.rating for review in self.reviews_list])
            return total / len(self.reviews_list)

    @classmethod
    def highest_rated(cls):
        if len(cls.all) == 0:
            return None
        else:
            return max(cls.all, key=lambda x: x.average_rating())

from .Review import Review





# class Movie:
#     def __init__(self, title):
#         pass

#     # title property goes here!

#     def reviews(self):
#         pass

#     def reviewers(self):
#         pass

#     def average_rating(self):
#         pass

#     @classmethod
#     def highest_rated(cls):
#         pass
