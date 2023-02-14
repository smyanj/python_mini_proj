# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


# Create other functions for:
#   - listing movies
def listing_movies():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release Date: {movie['year']}")
#   - finding movie
def finding_movies():
    search_movies = input("Please enter the movie title you are searching for: ")
    for movie in movies:
        if movie["Title"] == search_movies:
            print_movie(movie)
# And another function here for the user menu
#def user_menu
def user_menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add_movie()
        elif selection == "l":
            listing_movies()
        elif selection == "f":
            finding_movies()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!
user_menu()