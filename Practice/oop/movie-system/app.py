from movie import Movie
from user import User

user = User("elijah")

my_movie = Movie("The matrix", "sci-fi", False)

user.movies.append(my_movie)

print(user.watched_movies())