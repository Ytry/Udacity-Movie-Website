import webbrowser


class Movie():
    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
        """"
        constructor of the movie class
        initializes parameters needed in entertainment center class
        """"
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """"
        Test function for class variables
        opens a new browser tab with a given string as the url
        """"
        webbrowser.open(self.trailer_youtube_url)
