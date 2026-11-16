from add_book import add_book 
from diaplay_books import display_books
from register_student import register_student
from delete_book import delete_book
from search_books import search_books
from issue_book import issue_book 
from display_issued_books import display_issued_books
from return_book import return_book
def main():
    while True:
        print("LIBRARY MANAGEMENT SYSTEM")
        print("i. add new book")
        print("ii. display all books")
        print("iii. search for a book")
        print("iv. register a student") 
        print("v. issue a book")
        print("vi. return a book")
        print("vii. display the issued books") 
        print("viii. delete a book") 

        choice = input("enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            register_student() 
        elif choice == "5":
            issue_book() 
        elif choice == "6":
            return_book()    
        elif choice == "7":
            display_issued_books()
        elif choice == "8":
            delete_book()
            print("thank you for using library management system")
            break
        else:
            print("invalid choice! please try again.")
main()