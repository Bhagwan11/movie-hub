import webbrowser

'''---------Creating the Class Movie to hold movie details and links---------'''

class Movie:

    #Movie constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #method to play trailer
    def showtrailer(self):

        webbrowser.open(self.trailer)

    
