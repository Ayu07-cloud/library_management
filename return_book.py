from import_file import load_data,save_data,B_FILE,C_FILE
def return_book():
    books = load_data(B_FILE)
    issued = load_data(C_FILE)

    student_id = input("enter student id: ")
    book_id = input("enter book id: ")

    found = False

    for record in issued:
        if (record["student_id"].lower() == student_id.lower()
        and record["book_id"].lower() == book_id.lower()):
            
            found = True

            for book in books:
                if book["book_id"].lower() == book_id.lower():
                    book["available_copies"] += 1
                    break
            issued.remove(record)
            break
    if found:
        save_data(B_FILE, books)
        save_data(C_FILE, issued)
        print("book returned successfully")
    else:
        print("no issue record found")
