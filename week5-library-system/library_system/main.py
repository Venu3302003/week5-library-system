from library_system.library import Library

def main():
    lib = Library()

    while True:
        print("\nLIBRARY MANAGEMENT SYSTEM")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            t = input("Title: ")
            a = input("Author: ")
            i = input("ISBN: ")
            y = input("Year: ")
            lib.add_book(t, a, i, y)

        elif choice == "2":
            n = input("Name: ")
            m = input("Member ID: ")
            lib.register_member(n, m)

        elif choice == "3":
            i = input("ISBN: ")
            m = input("Member ID: ")
            print(lib.borrow_book(i, m))

        elif choice == "4":
            i = input("ISBN: ")
            m = input("Member ID: ")
            print(lib.return_book(i, m))

        elif choice == "5":
            for book in lib.books.values():
                print(book)

        elif choice == "6":
            lib.save_data()
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
