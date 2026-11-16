from import_file import load_data,save_data,B_FILE,C_FILE
def delete_book():
    books = load_data(B_FILE)
    issued = load_data(C_FILE)
    book_id = input("enter book id to delete:")

    found = False

    for record in issued:
        if record["book_id"].lower() == book_id.lower():
            print("book is currently issued and cannot be deleted")
            return
    for book in books:
        if book["book_id"].lower() == book_id.lower():
            books.remove(book)
            found = True
            break
    if found:
        save_data(B_FILE, books)
        print("book deleted successfully")
    else:
        print("book not found")
