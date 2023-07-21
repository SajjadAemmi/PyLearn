import sqlite3

def show_menu():
    print("1- show list")
    print("2- add new")
    print("3- edit")
    print("4- remove")


def load_database():
    global connection
    global my_cursor
    connection = sqlite3.connect("chinook.db")
    my_cursor = connection.cursor()


def show_list():
    # for data in my_cursor.execute("SELECT * FROM customers WHERE Country = 'France'"):
    #     print(data)
    result = my_cursor.execute('SELECT * FROM genres')
    moshtariane_almani = result.fetchall()
    for moshtari in moshtariane_almani:
        print(moshtari)

def add_new():
    new_genre_name = input("enter a name for your new genre: ")
    my_cursor.execute(f"INSERT INTO genres(Name) VALUES('{new_genre_name}')")
    connection.commit()

def edit():
    new_city = input()
    my_cursor.execute(f"UPDATE customers SET City='{new_city}', Country='Iran' WHERE FirstName='Helena' AND CustomerId=6")
    connection.commit()

def remove():
    genre_name = input("enter genre name: ")
    my_cursor.execute(f"DELETE FROM genres WHERE Name = '{genre_name}'")
    connection.commit()


load_database()
while True:
    show_menu()
    choice = int(input())

    if choice == 1:
        show_list()
    elif choice == 2:
        add_new()
    elif choice == 3:
        edit()
    elif choice == 4:
        remove()
