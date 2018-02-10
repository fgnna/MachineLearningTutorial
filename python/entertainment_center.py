import fresh_tomatoes
#是
import media
toy_story = media.Movie("Toy Story",
                        "A story of a boy and x......",
                        "http://www.imageto.org/images/5GKJ0.jpg",
                        "http://www.dytt8.net/html/gndy/dyzz/20180110/56050.html")

print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.imageto.org/images/UqWbc.jpg",
                     "http://www.dytt8.net/html/gndy/dyzz/20180110/56049.html")


movies = [toy_story, avatar]
print avatar.__doc__
print avatar.__module__
#fresh_tomatoes.open_movies_page(movies)
