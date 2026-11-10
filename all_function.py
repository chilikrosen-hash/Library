from data import books

def display_books(books):
    for book in books:
        print(book)

def search_book(books,name):
    for book in books:
        if name in book["name"].lower().strip():
            return book
        

def add_books(books,name,author,year):
    new_book = {}
    for book in books:
        if book["name"].lower().strip().replace(" ","") == name.lower().strip().replace(" ","") and book["author"].lower().strip().replace(" ","")== author.lower().strip().replace(" ",""):
            return False
    new_book["id"] = get_next_book_id(books)
    new_book["name"]=name
    new_book["author"]=author
    new_book["year"] = year
    new_book["available"] = True
    books.append(new_book)
    return True

def Borrow_book(books,book_id):
    for book in books:
        if book["id"] == book_id and book["available"] == True:
            book["available"] = False
            return True

    return False

def return_book(books,book_id):
    for book in books:
        if book["id"] == book_id and book["available"] == False:
            book["available"] = True
            return True
    return False

def get_available(books):
    available_books = []
    for book in books:
        if book["available"] == True:
            available_books.append(book["name"])

    return available_books

def get_books_by_author(books,author):
    books_list = []
    for book in books:
        if book["author"].lower().strip().replace(" ","") == author.lower().strip().replace(" ",""):
            books_list.append(book)
    return books_list

def get_next_book_id(books):
    return books[-1]["id"] + 1



