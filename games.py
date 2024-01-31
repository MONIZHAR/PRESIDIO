import sqlite3

# Function to create the database table if it doesn't exist
def create_table():
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            genre TEXT,
            year INTEGER
        )
    ''')

    conn.commit()
    conn.close()

# Function to insert a new game into the database
def add_game(title, genre, year):
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO games (title, genre, year) VALUES (?, ?, ?)", (title, genre, year))

    conn.commit()
    conn.close()

# Function to retrieve all games from the database
def get_all_games():
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM games")
    games = cursor.fetchall()

    conn.close()

    return games

# Function to search for games based on criteria
def search_games(criteria, value):
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM games WHERE {criteria} = ?"
    cursor.execute(query, (value,))
    result = cursor.fetchall()

    conn.close()

    return result

# Main application logic
def main():
    create_table()

    # Adding initial games for testing
    add_game("The Witcher 3: Wild Hunt", "Action RPG", 2015)
    add_game("Red Dead Redemption 2", "Action-Adventure", 2018)
    add_game("Cyberpunk 2077", "Action RPG", 2020)

    while True:
        print("\nMain Menu:")
        print("1. Display all games")
        print("2. Add a new game")
        print("3. Search for games")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            games = get_all_games()
            if not games:
                print("No games saved.")
            else:
                for game in games:
                    print(f"ID: {game[0]}, Title: {game[1]}, Genre: {game[2]}, Year: {game[3]}")

        elif choice == '2':
            title = input("Enter the title of the game: ")
            genre = input("Enter the genre of the game: ")
            year = input("Enter the release year of the game: ")

            add_game(title, genre, year)
            print("Game added successfully.")

        elif choice == '3':
            criteria = input("Enter search criteria (title, genre, year): ")
            value = input(f"Enter the {criteria} to search for: ")

            result = search_games(criteria, value)
            if not result:
                print("No matching games found.")
            else:
                for game in result:
                    print(f"ID: {game[0]}, Title: {game[1]}, Genre: {game[2]}, Year: {game[3]}")

        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
