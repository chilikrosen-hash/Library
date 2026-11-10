from all_function import add_books
from data import books
def get_name():
    is_exist = False
    while not is_exist:
        user_input_name = input("please enter a book name ")
        if user_input_name:
            is_exist = True
            return user_input_name
def get_author():
    is_exist = False
    while not is_exist:
        user_input_author = input("please enter a book author ")
        if user_input_author:
            is_exist = True
            return user_input_author

def get_positive_num():
    is_positive = False
    while not is_positive:
        user_input = input("please enter a positive num ")
        if user_input.isdigit() and int(user_input) > 0:
            is_positive = True

    return int(user_input)

