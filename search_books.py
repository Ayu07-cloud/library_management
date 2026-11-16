from import_file import load_data,B_FILE
def search_books():
    books = load_data(B_FILE)
    print("->search id")
    print("->search name")
    print("->search author")

    choice = input("enter choice:")
    value = input("enter search value:").lower()

    found = False

    for book in books:
        if choice == "1" and book["book_id"].lower() == value:
            print(book)
            found = True
            break
        elif choice == "2" and value in book["book_name"].lower():
            print(book)
            found = True
            break
        elif choice == "3" and value in book["author"].lower():
            print(book)
            found = True
            break
    if not found:
        print("book not found")
