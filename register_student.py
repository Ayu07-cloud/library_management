from import_file import load_data,save_data,S_FILE
def register_student():
    students = load_data(S_FILE)
    student_id = input("enter student id:")

    for student in students:
        if student["student_id"].lower() == student_id.lower():
            print("student id already exists")
            return
    name = input("enter student name:")
    department = input("enter department:")
    contact = input("enter contact number:")
    new_student = {
        "student_id": student_id,
        "name": name,
        "department": department,
        "contact": contact
    }
    students.append(new_student)
    save_data(S_FILE, students)
    print("student registered successfully")