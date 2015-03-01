import webbrowser

class Movie(object):
	"""Movies contain a title, storyline, poster image, rating and trailer data"""
	VALID_RATINGS = ["G", "PG", "PG-13", "M", "R"]

	def __init__(self, title, storyline, poster_image_url, rating, trailer_youtube_url):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.rating = rating
		self.trailer_youtube_url = trailer_youtube_url

		def show_trailer_youtube():
			'''Open a web browser to the youtube url for the movie trailer. '''
			webbrowser.open(self.trailer_youtube_url)
		
