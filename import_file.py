 
import json
import os

B_FILE = "books.json"
S_FILE = "stdnt.json"
C_FILE = "issued_book.json"

def create_files():

    if not os.path.exists(B_FILE):
        with open(B_FILE, "w") as file:
            json.dump([], file, indent=4)

    if not os.path.exists(S_FILE):
        with open(S_FILE, "w") as file:
            json.dump({}, file, indent=4)

    if not os.path.exists(C_FILE):
        with open(C_FILE, "w") as file:
            json.dump([], file, indent=4)

def load_data(f):
    with open(f, "r") as file:
        data = json.load(file)
    return data

def save_data(f, data):
    with open(f, "w") as file:
        json.dump(data, file, indent=4)
