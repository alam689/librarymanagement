import add_books
import view_all_books
import update_book
import remove_book

all_books = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. Book Update")
    print("3. Book Remove")
    print("4. View All Books")

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        all_books = update_book.update_book(all_books)
    elif menu == "3":
        all_books = remove_book.remove_book(all_books)
    elif menu == "4":
        view_all_books.view_all_books(all_books)
    else:
        print("Choose a valid number")