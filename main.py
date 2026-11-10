from all_function import *
from data import *
from menu import *
from input_user import *


def main():
    is_exist = False
    while not is_exist:
        menu()
        user_choice = input("please chose number between 1 - 8 ")
        if user_choice == "8":
            is_exist == True
            break
        if int(user_choice) > 8 or  int(user_choice) <=0:
            user_choice = input("invalid choice please try again ")
        if user_choice == "1":
            display_books(books)
        elif user_choice == "2":
            print(search_book(books,get_name()))
        elif user_choice =="3":
            print(add_books(books,get_name(),get_author(),get_positive_num()))
        elif user_choice == "4":
            print(Borrow_book(books,get_positive_num()))
        elif user_choice == "5":
            print(return_book(books,get_positive_num()))
        elif user_choice =="6":
            print(get_available(books))
        elif user_choice =="7":
            print(get_books_by_author(books,get_author()))

if __name__ == "__main__":
    main() 

        