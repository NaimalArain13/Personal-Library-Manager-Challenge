import json

library = []

#display menu function 
def display_menu():
    print("\n📚 Personal Library Manager")
    print("1. Add a book:")
    print("2. Remove a book:")
    print("3. Search for a book:")
    print("4. Display all books:")
    print("5. Display statistics:")
    print("6. Exit:")
    
# Add a book
def add_book():
      title = input("Enter the book title: ")
      author = input("Enter the author: ")
      publication_year = input("Enter the publication year: ")
      genre = input("Enter the genre: ")
      read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
       
      book = {
        "title": title,
        "author": author,
        "year": publication_year,
        "genre": genre,
        "read": read
        }     
      library.append(book)
      print(f"{book['title']} added successfully ✔.")
    
#remove book
def remove_book():
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
           library.remove(book)
           print(f"{book['title']} removed successfully ❌.")
           return
    print("No book found!")
           
#search for a book
def search_book():
    search_by = input("Search by (1) Title or (2) Author? ").strip()
    
    if search_by == "1":
        query = input("Enter book title: ").strip()
        result = [book for book in library if query.lower() in book["title"].lower()]
    elif search_by == "2":
        query = input("Enter book's author: ").strip()
        result = [book for book in library if query.lower() in book["author"].lower()]
    else:
        print("Invalid choice!")
        return

    if result:
        print("\n📖 Matching Books:")
        for book in result:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("❌ No matching books found.")
        
#display all books
def display_library():
    if not library:
        print("📭 Your library is empty.")
        return
    
    print("\n 📚 Your Library")
    for index, book in enumerate(library, start=1):
        print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
     
#display statistics   
def display_statistics():
    total_books = len(library)
    if total_books == 0:
        print("📭 No books in the library.")
        return
    
    read_books = sum(1 for book in library if book["read"])
    read_percentage = (read_books / total_books) * 100
    
    print(f"\n📊 Library Statistics:")
    print(f"Total Books: {total_books}")
    print(f"Percentage Read: {read_percentage:.2f}%")
    
#save library
def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file)
        print("📁 Library saved successfully!")

#load library
def load_library():
    global library
    try:
        with open("library.json", "r") as file:
            library = json.load(file)
    except FileNotFoundError:
        library = []
    except json.JSONDecodeError:
        print("❌ Error decoding JSON. The library file may be corrupted.")
        library = []