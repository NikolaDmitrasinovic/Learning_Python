current_movies = {'The Grinch' : '11:00am',
                  'Rudolph' : '1:00pm',
                  'Piano' : '3:00',
                  "River's Edge" : "5:00pm"}

print("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like to showtime for?\n")
showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, "is playing at", showtime)
    