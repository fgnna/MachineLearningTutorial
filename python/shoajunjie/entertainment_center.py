# -- coding: utf-8 --
import fresh_tomatoes
#
import media

#我的电影集，三个等级各一个
movies = [media.MovieG("Toy Story",
                        "A story of a boy and x......",
                        "http://www.imageto.org/images/5GKJ0.jpg",
                        "http://player.youku.com/embed/XMzExNDQzNjE4NA=="),
          media.MoviePG("Avatar",
                        "A marine on an alien planet",
                        "http://www.imageto.org/images/UqWbc.jpg",
                        "http://player.youku.com/embed/XMzExNDQzNjE4NA=="),
          media.MovieR("Avatar",
                        "A marine on an alien planet",
                        "http://www.imageto.org/images/UqWbc.jpg",
                        "http://player.youku.com/embed/XMzExNDQzNjE4NA==")
          ]

#生成我的网站
fresh_tomatoes.open_movies_page(movies)
