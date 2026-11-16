import json
import os

B_FILE = "books.json"
S_FILE = "stdnt.json"
C_FILE = "issued_book.json"

def load_data(f):
    with open(f, "r") as file:
        data = json.load(file)
    return data
def save_data(f , data):
    with open(f , "w") as file:
        json.dump(data, file, indent=4)