import media
import fresh_tomatoes


# instance of the movie class for hunger games
hunger_games = media.Movie("Hunger Games",
                           "http://vignette4.wikia.nocookie.net/thehungergames/images/b/b8/Hungergames_poster.jpg/revision/latest/scale-to-width-down/220?cb=20120329195535&format=webp",  # noqa
                           "https://www.youtube.com/watch?v=PbA63a7H0bo&ab_channel=MovieclipsTrailers")  # noqa

# instance of the movie class for catching fire
catching_fire = media.Movie("Hunger Games: Catching Fire",
                            "http://vignette2.wikia.nocookie.net/thehungergames/images/7/76/Catching_Fire.jpg/revision/latest/scale-to-width-down/220?cb=20091007051512&format=webp",  # noqa
                            "https://www.youtube.com/watch?v=EAzGXqJSDJ8&ab_channel=MovieclipsTrailers")  # noqa

# instance of the movie class for mocking jay
mocking_jay = media.Movie("Mocking Jay Pt: 1",
                          "http://vignette1.wikia.nocookie.net/thehungergames/images/1/11/MockingjayCover.jpg/revision/latest/scale-to-width-down/220?cb=20100211200124&format=webp",  # noqa
                          "https://www.youtube.com/watch?v=C_Tsj_wTJkQ&ab_channel=TheHungerGames")  # noqa

# list of movie instances
movies = [hunger_games, catching_fire, mocking_jay]

# fresh tomatoes function taking in my list movies as a paramater
fresh_tomatoes.open_movies_page(movies)
