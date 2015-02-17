import media
import fresh_tomatoes

# Add data for each movie to be listed
# 
# movie_name = media.Movie("Title",
#                          "Storyline",
#                          "URL to poster image",
#                          "Rating",
#                          "URL to youtube.com movie trailer")


star_wars = media.Movie("Star Wars - Episode IV A New Hope",
						"Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a wookiee and two droids to save the universe from the Empire's world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader.",
						"https://image.tmdb.org/t/p/original/tvSlBzAdRE29bZe5yYWrJ2ds137.jpg",
						"PG",
						"http://youtu.be/9gvqpFbRKtQ")

lotr_tfotr = media.Movie("Lord of the Rings - The Fellowship of the Ring",
						"A meek hobbit of the Shire and eight companions set out on a journey to Mount Doom to destroy the One Ring and the dark lord Sauron.",
						"https://image.tmdb.org/t/p/original/9HG6pINW1KoFTAKY3LdybkoOKAm.jpg",
						"PG",
						"http://youtu.be/V75dMMIW2B4")

true_romance = media.Movie("True Romance",
						   "Clarence marries hooker Alabama, steals cocaine from her pimp, and tries to sell it in Hollywood, while the owners of the coke try to reclaim it.",
						   "https://image.tmdb.org/t/p/original/bkJMxpzunO6q0pAdLUR6mCQngAZ.jpg",
						   "R",
						   "http://youtu.be/_wNYNDzKpuQ")

top_gun = media.Movie("Top Gun",
					  "As students at the Navy's elite fighter weapons school compete to be best in the class, one daring young flyer learns a few things from a civilian instructor that are not taught in the classroom.",
					  "https://image.tmdb.org/t/p/original/9miZUkG0TLfrDJt68JvXttxLu9S.jpg",
					  "PG-13",
					  "http://youtu.be/qAfbp3YX9F0")

pulp_fiction = media.Movie("Pulp Fiction",
					  	   "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
					  	   "https://image.tmdb.org/t/p/original/dM2w364MScsjFf8pfMbaWUcWrR.jpg",
					  	   "R",
					  	   "http://youtu.be/s7EdQ4FqbhY")

fury = media.Movie("Fury",
				   "April, 1945. As the Allies make their final push in the European Theatre, a battle-hardened Army sergeant named Wardaddy commands a Sherman tank and his five-man crew on a deadly mission behind enemy lines. Outnumbered, out-gunned, and with a rookie soldier thrust into their platoon, Wardaddy and his men face overwhelming odds in their heroic attempts to strike at the heart of Nazi Germany.",
				   "https://image.tmdb.org/t/p/original/il9XWx5CbNd2KdDUwrcClEZiLkv.jpg",
				   "PG-13",
				   "http://youtu.be/-OGvZoIrXpg")

the_matrix = media.Movie("The Matrix",
				   "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
				   "https://image.tmdb.org/t/p/original/gynBNzwyaHKtXqlEKKLioNkjKgN.jpg",
				   "M",
				   "http://youtu.be/m8e-FF8MsqU")

the_300 = media.Movie("300",
				      "King Leonidas and a force of 300 men fight the Persians at Thermopylae in 480 B.C.",
				      "https://image.tmdb.org/t/p/original/bYR8O1H1ZlME7Dm9ysfTYZnRDpw.jpg",
				      "M",
				      "http://youtu.be/UrIbxk7idYA")

watchmen = media.Movie("Watchmen ",
				      "In an alternate 1985 where former superheroes exist, the murder of a colleague sends active vigilante Rorschach into his own sprawling investigation, uncovering something that could completely change the course of history as we know it.",
				      "https://image.tmdb.org/t/p/original/jXggcKzlyxj7yMBUIsqwiaaEtD5.jpg",
				      "R",
				      "http://youtu.be/PVjA0y78_EQ")

# Store movies in an array to send to the fresh tomatoes script
movies = [star_wars, lotr_tfotr, true_romance, top_gun, pulp_fiction, fury, the_matrix, the_300, watchmen]

# Send the array of movies to the fresh tomatoes web page builder.
fresh_tomatoes.open_movies_page(movies)
