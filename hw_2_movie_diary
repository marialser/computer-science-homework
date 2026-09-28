movies = []
def add_movie():
    title = input("Movie Title: ").title()
    director = input("Director: ").title()
    while True:
        try:
            year = int(input("Year it was released: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    date = input("Date you watched it: ")
    while True:
        try:
            rating = float(input("Your rating (1-10): "))
            if 1 <= rating <= 10:
                break
            else:
                print("Rating must be between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")
    review = input("Your review: ")
    movie = {
            "title": title,
            "director": director,
            "year": year,
            "date": date,
            "rating": rating,
            "review": review
        }
    movies.append(movie)


def view_all_movies():
    for movie in movies:
        print("--------------------")
        print(movie["title"], f"({movie['year']})")
        print("Director:", movie["director"])
        print("Watched:", movie["date"])
        print("Rating:", movie["rating"], "/10")
        print("Review:", movie["review"])
    print("--------------------")


def highest_rated():
    highest = movies[0]
    for movie in movies:
        if movie["rating"] >highest["rating"]:
            highest = movie
    print(highest["title"], "-", highest["rating"])


def lowest_rated():
    lowest = movies[0]
    for movie in movies:
        if movie["rating"] < lowest["rating"]:
            lowest = movie
    print(lowest["title"], "-", lowest["rating"])


def search_movie():
    search = input("Enter movie title: ")
    found = False
    for movie in movies:
        if movie["title"].lower() == search.lower():
            print("--------------------")
            print(movie["title"], f"({movie['year']})")
            print("Director:", movie["director"])
            print("Watched:", movie["date"])
            print("Rating:", movie["rating"], "/10")
            print("Review:", movie["review"])
            found = True
    if not found:
        print("Movie not found.")

def menu():   
    while True:
        print("Choose what you want to do:")
        print("1. Add a movie")
        print("2. View all watched movies")
        print("3. View the highest rated movie")
        print("4. View the lowest rated movie")
        print("5. Find a watched movie")
        print("6. Exit")
        choice = input().strip(" ")[0]
        if choice == "1":
            add_movie()
        elif choice == "2":
            view_all_movies()
        elif choice == "3":
            highest_rated()
        elif choice == "4":
            lowest_rated()
        elif choice == "5":
            search_movie()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option.")

print("Welcome to your Movie Diary!")
menu()
