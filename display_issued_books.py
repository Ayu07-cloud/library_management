from import_file import load_data,C_FILE
def display_issued_books():
    issued = load_data(C_FILE)

    if len(issued) == 0:
        print("no books are currently issued")
        return
    print("ISSUED BOOKS")
    for record in issued:
        print("student id:", record["student_id"])
        print("book id:", record["book_id"])
        print("issue date:", record["issue_date"])
