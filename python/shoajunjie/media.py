# -- coding: utf-8 --
import webbrowser


class Movie:

    """ 电影级别分类常量 """
    VALID_RATINGS = ["G", "PG", "R"]

    """ 初始化 """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youku):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer_youku

    """ 打网预告网页 """
    def show_trailer(self):
        webbrowser.open(self.trailer_url)


class MovieG(Movie):
    """ G级电影子类 """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youku):
        Movie.__init__(self, movie_title+"("+Movie.VALID_RATINGS[0]+" level)", movie_storyline, poster_image, trailer_youku)


class MoviePG(Movie):
    """ PG级电影子类 """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youku):
        Movie.__init__(self, movie_title + "(" + Movie.VALID_RATINGS[1] + " level)", movie_storyline, poster_image,
                       trailer_youku)


class MovieR(Movie):
    """ R级电影子类 """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youku):
        Movie.__init__(self, movie_title + "(" + Movie.VALID_RATINGS[1] + " level)", movie_storyline, poster_image,
                       trailer_youku)
