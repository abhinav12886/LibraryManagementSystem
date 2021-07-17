# Make a library class and define methods(displayBook(list),lendBook(asksNameOfPersonWhoOwnsIt),
# add_book, return_book(if somebody wants to return the book),
# Constructor => Harry_library = Library(List_of_books, library_name)

# maintain a dictionary of 'who lends the book' (key = books, value = name_of_person)

# create a main file asking users to input what they want (display book, lend book, return book,add book)
# with the help of infinite while loop.

class library:

    @staticmethod
    def display_book():
        """
        it will display all the available book from the list_of_book
        """
        print("\nAll the available books are:- ", list_of_book, "\n")

    @staticmethod
    def add_book():
        """
        as donation
        it will add_books to the list_of_books taking book name as input from user
        """
        user_input = input("\nEnter the book name which you want to donate:- \n")
        user_input = user_input.lower()

        list_of_book.append(user_input)  # it will append the new book to the list of books..
        print(f"Your book '{user_input}' has been added. \n")
        print("updated list of books:- ", list_of_book)

    @staticmethod
    def lend_book():
        """
        it will create a dictionary of user who lends the book
        with key = person name ; value = list of book name
        and remove the lend book from the list_of_books
        """
        user_input = int(input(print("Enter number of books you want to lend\n")))
        list1 = []

        k = input("enter your name")
        k = k.lower()

        for i in range(user_input):  # this loop will take input the book_name and append it to the list1
            v = input("Enter the name of the book")
            v = v.lower()
            list1.append(v)

        dict = {k: list1}  # it will indicate who has taken which book...
        print(dict)

        # removing the lend book from the list_of_books
        for i in list1:
            list_of_book.remove(i)
        print("Now available books are:- ", list_of_book)

    @staticmethod
    def return_book():
        """
        it will take person name and book_name as key-value pair and remove that key-value pair from the
        lend_book dictionary, and will append the book_name(Key) back to the lis_of_books.
        """
        user_input = int(input(print("Enter number of books you want to return\n")))
        list1 = []
        k = input("enter your name")
        k = k.lower()

        for i in range(user_input):
            v = input("Enter the name of the book")
            v = v.lower()
            list1.append(v)

        dict = {k: list1}  # it will print the list of lend books in front of person names...
        print("dictionary", dict)

        for k, list1 in list(dict.items()):  # this loop will delete the name from the lend book dictionary..
            dict.pop(k, None)

        print(f"Your name '{k}' and your book '{list1}' has been removed from the lend book list"
              f" new updated list is :- ", dict)


list_of_book = ["harry potter", "devil", "secret", "silence", "ncert", "physics", "maths", "biology"]

Library = library()  # class object

dict = {}  # empty dictionary containing person name and book name after calling lend_book function

# while loop to keep the program running till the user want it to...
while True:
    user_input = int(input(print("Please, Enter the number corresponding to available options\n",
                                 "(1) for displaying all the available books \n"
                                 " (2) for donate book \n"
                                 " (3) for lending a book\n"
                                 " (4) for returning a book\n"
                                 " else if you want to exit the program press (5)")))

    if user_input == 1:
        Library.display_book()
    elif user_input == 2:
        Library.add_book()
    elif user_input == 3:
        Library.lend_book()
    elif user_input == 4:
        Library.return_book()
    else:
        break
