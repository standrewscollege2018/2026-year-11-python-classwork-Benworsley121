'''favourite movies'''

#favouritemovie = input("what is your favourite movie")
#secondfavouritemovie = input("what is your second favourite movie")
#thirdfavouritemovie = input("what is your third favourite movie")

#print(f" your favourite movies are {favouritemovie}, {secondfavouritemovie}, {thirdfavouritemovie}")


movies =[]

for i in range(3):
    movie = input("enter a favourite movie")
    movies.append(movie)

print(movies)

for j in range(len(movies)):
    print( f"{i+1} {movies[j]}")