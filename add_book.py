from import_file import load_data,save_data,B_FILE
def add_book():
    books = load_data(B_FILE)
    book_id = input("enter book id:")

    for book in books:
        if book["book_id"].lower() == book_id.lower():
            print("book id already exists")
            return
    book_name = input("enter book name:")
    author = input("enter author name:")
    category = input("enter category:")
    try:
        copies = int(input("enter Number of copies:"))
        if copies <= 0:
            print("copies must be greater than zero")
            return
    except ValueError:
        print("please enter a valid number")
        return
    book = {
        "book_id": book_id,
        "book_name": book_name,
        "author": author,
        "category": category,
        "available_copies": copies
    }
    books.append(book)
    save_data(B_FILE, books)
    print("book added successfully")