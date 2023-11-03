from movies import Movies

movies = Movies('./movies.txt')

# Defining the function for the main menu
def main_menu():
    while True:
        # Displaying the menu options
        print("Welcome to the Movie Database!")
        print("Menu Options:")
        print("1. View Movies")
        print("2. Search for a Movie")
        print("3. List All Movie Names")
        print("4. Search Movies by Name")
        print("5. Search Movies by Cast")
        print("q. Quit")

        # Get user's choice
        choice = input("Select an option: ")

        if choice == "1":
            # Implement logic to view movies
            for movie in movies.get_movies():
                print(f"Movie: {movie['name']}")
                print(f"Cast: {', '.join(movie['cast'])}")
        elif choice == "2":
            # Implement logic to search for a movie
            search_term = input("Enter a movie name to search for: ")
            found_movies = movies.search_movies(search_term)
            if found_movies:
                for movie in found_movies:
                    print(f"Movie: {movie['name']}")
                    print(f"Cast: {', '.join(movie['cast'])}")
            else:
                print("No matching movies found.")
        elif choice == "3":
    movie_names = [movie['name'] for movie in movies.get_movies()]
    if movie_names:
        print("List of Movie Names:")
        for name in movie_names:
            print(name)
    else:
        print("No movies in the database.")
        elif choice == "4":
    search_word = input("Enter a search word: ")
    matching_movies = [movie for movie in movies.get_movies() if search_word.lower() in movie['name'].lower()]
    if matching_movies:
        print("Matching Movies:")
        for movie in matching_movies:
            print(movie['name'])
    else:
        print("No matching movies found.")
        elif choice == "5":
    search_word = input("Enter a search word: ")
    matching_movies = [movie for movie in movies.get_movies() if any(search_word.lower() in actor.lower() for actor in movie['cast'])]
    matching_actors = list(set([actor for movie in matching_movies for actor in movie['cast'] if search_word.lower() in actor.lower()]))
    if matching_movies:
        print("Matching Movies:")
        for movie in matching_movies:
            print(movie['name'])
        
        print("Matching Actors/Actresses:")
        for actor in matching_actors:
            print(actor)
    else:
        print("No matching movies or cast members found.")
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
