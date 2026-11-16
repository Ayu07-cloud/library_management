from import_file import load_data,B_FILE
def display_books():
    books = load_data(B_FILE)

    if len(books) == 0:
        print("no books available")
        return
    for book in books:
        print("book  id:", book["book_id"])
        print("book name:", book["book_name"])
        print("author:", book["author"])
        print("category:", book["category"])
        print("available copies:", book["available_copies"])