#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Percy Jackson & the Olympians: The Lightning Thief"

print("My favorite movie is "+favMovie+"\n")


#Part 3 Investigate the data
#print(movieData.head())
#print(movieData["movie_title"])

#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information

favBoolList = movieData["movie_title"] == favMovie

favMovieData = movieData.loc[favBoolList]
print(favMovieData)

print("\n\n")

#Create a new variable to store a new data set with a certain genre
genreBoolList = movieData["genres"].str.contains("Science Fiction & Fantasy")
genreMovieData = movieData.loc[genreBoolList]

movieNum = genreMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Science Fiction & Fantasy in the data set.\n")
print("There are " + str(movieNum) + " movies under the category Science Fiction & Fantasy.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
rating = int(favMovieData["audience_rating"])
#min
min = genreMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated "+ str(rating-min) +" points higher than the lowest rated movie.")
print()

#find max
max = genreMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated "+ str(max-rating) +" points lower than the highest rated movie.")
print()

#find mean
mean = genreMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is lower than the mean movie rating.")

#find median
median = genreMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is lower than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(genreMovieData["audience_rating"], range = (0, 100), bins = 20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Science Fiction & Fantasy Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Science Fiction & Fantasy Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, over 140 movies are rated around 55-60."
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = genreMovieData, x= "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating versus Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, when the audience rating goes up, the critic rating goes up in a positive correlation."
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
