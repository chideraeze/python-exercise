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
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
