# Declare a dictionary called "movie" with movie genres and the number of students who watched each genre.
movie={"Comedy": 73, "Action": 42, "Romance":38, "Fantasy": 28, "Science-fiction": 22,
       "Horror": 19, "Crime": 18, "Documentary": 12, "History": 8, "War": 7}
# Create a list called "movie_genres" containing the keys of the "movie" dictionary.
# Create a list called "students_number" containing the values of the "movie" dictionary.
movie_genres=list(movie.keys())
students_number=list(movie.values())
# Print the "movie" dictionary to the console.
print(movie)
import matplotlib.pyplot as plt
# Plot a pie chart using "students_number" as the data, "movie_genres" as the labels and display the percentage using the "autopct" argument.
plt.pie(students_number, labels=movie_genres, autopct='%1.1f%%')
# Display the pie chart on the screen.
plt.show()
# Declare a variable called "requested_genre" and assign it the value of a movie genre from the input list (e.g. "Comedy").
requested_genre = "Comedy" # Modify this variable to change the requested genre.
# Print the value in the "movie" dictionary that corresponds to the "requested_genre" key to the console (e.g. "73" if "requested_genre" is "Comedy").
print(movie[requested_genre])