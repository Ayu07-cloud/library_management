from import_file import load_data,save_data,B_FILE,S_FILE,C_FILE
def issue_book():
    books = load_data(B_FILE)
    students = load_data(S_FILE)
    issued = load_data(C_FILE)

    student_id = input("enter student id:")
    book_id = input("enter book id:")

    student_found = False
    book_found = False

    for student in students:
        if student["student_id"].lower() == student_id.lower():
            student_found = True
            break
    for book in books:
        if book["book_id"].lower() == book_id.lower():
            book_found = True
            break
    if not student_found:
        print("student is not registered")
        return
    if not book_found:
        print("book not found")
        return
    if book["available_copies"] <= 0:
        print("book is not available")
        return

    book["available_copies"] -= 1
    issue_date = input("enter issue date (dd/mm/yyyy):")
    record = {
        "student_id": student_id,
        "book_id": book["book_id"],
        "issue_date": issue_date
    }
    issued.append(record)
    save_data(B_FILE, books)
    save_data(C_FILE, issued)
    print("book's been issued successfully")