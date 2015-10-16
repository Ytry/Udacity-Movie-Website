import media
import fresh_tomatoes


# instance of the movie class for hunger games
hunger_games = media.Movie("Hunger Games",
                           "http://goo.gl/nCsp2X",
                           "https://goo.gl/vJaDPO")

# instance of the movie class for catching fire
catching_fire = media.Movie("Hunger Games: Catching Fire",
                            "http://goo.gl/b6K5FK",
                            "https://goo.gl/KmezpX")

# instance of the movie class for mocking jay
mocking_jay = media.Movie("Mocking Jay Pt: 1",
                          "http://goo.gl/hDerDm",
                          "https://goo.gl/uvOsFo")

# list of movie instances
movies = [hunger_games, catching_fire, mocking_jay]

# fresh tomatoes function taking in my list movies as a paramater
fresh_tomatoes.open_movies_page(movies)
