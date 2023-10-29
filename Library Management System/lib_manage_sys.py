class LibraryManagementSystem:

    def __init__(self):
        self.library_hash_table = {}
        self.users = {}
        self.datetime = __import__('datetime').datetime
        self.timedelta = __import__('datetime').timedelta

    def add_book(self):
        isbn = input("Enter ISBN: ")
        if isbn in self.library_hash_table:
            return "Book with this ISBN already exists!"
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        publication_year = int(input("Enter Publication Year: "))
        
        self.library_hash_table[isbn] = {
            "title": title,
            "author": author,
            "publication_year": publication_year,
            "status": "available",
            "checked_out_by": None,
            "due_date": None,
            "ratings": [],
            "avg_rating": "No ratings yet",
            "history": [],
            "reservations": []
        }
        return "Book added successfully!"

    def search_book(self):
        query = input("Enter book title or author to search: ")
        results = []
        for isbn, book in self.library_hash_table.items():
            if query in book["title"] or query in book["author"]:
                results.append(book)
        return results

    def checkout_book(self):
        isbn = input("Enter ISBN of the book to checkout: ")
        if isbn in self.library_hash_table:
            book = self.library_hash_table[isbn]
            if book["status"] == "available":
                user = input("Enter your name: ")
                book["status"] = "checked_out"
                book["checked_out_by"] = user
                book["due_date"] = self.datetime.now() + self.timedelta(days=14)
                book["history"].append((user, self.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                return f"Book checked out by {user}. Due date: {book['due_date']}."
            elif book["reservations"]:
                return f"Book is currently reserved by {book['reservations'][0]}."
            else:
                return "Book is currently checked out."
        else:
            return "Book with this ISBN doesn't exist!"

    def return_book(self):
        isbn = input("Enter ISBN of the book to return: ")
        if isbn in self.library_hash_table:
            book = self.library_hash_table[isbn]
            if book["status"] == "checked_out":
                book["status"] = "available" if not book["reservations"] else "reserved"
                book["checked_out_by"] = None
                book["due_date"] = None
                if book["reservations"]:
                    print(f"The book is now reserved for {book['reservations'][0]}.")
                return "Book returned successfully!"
            else:
                return "Book wasn't checked out."
        else:
            return "Book with this ISBN doesn't exist!"

    def renew_book(self):
        isbn = input("Enter ISBN of the book you want to renew: ")
        user = input("Enter your name: ")
        if isbn in self.library_hash_table:
            book = self.library_hash_table[isbn]
            if book["status"] == "checked_out" and book["checked_out_by"] == user:
                if not book["reservations"]:
                    book["due_date"] = self.datetime.now() + self.timedelta(days=14)
                    return f"Book renewed successfully. New due date: {book['due_date']}."
                else:
                    return f"Sorry, the book has been reserved by {book['reservations'][0]}. Please return it by the original due date."
            else:
                return "You haven't borrowed this book or it's not checked out."
        else:
            return "Book with this ISBN doesn't exist!"

    def reserve_book(self):
        isbn = input("Enter ISBN of the book you want to reserve: ")
        user = input("Enter your name: ")
        if isbn in self.library_hash_table:
            book = self.library_hash_table[isbn]
            if book["status"] == "available":
                return "Book is available. You don't need to reserve it."
            elif book["status"] == "checked_out" or book["status"] == "reserved":
                if user not in book["reservations"]:
                    book["reservations"].append(user)
                    return "Book reserved successfully."
                else:
                    return "You've already reserved this book."
            else:
                return "Invalid book status."
        else:
            return "Book with this ISBN doesn't exist!"

    def rate_book(self, isbn, user_name, rating):
        if isbn in self.library_hash_table:
            book = self.library_hash_table[isbn]
            if user_name in [hist[0] for hist in book['history']]:
                book["ratings"].append(rating)
                avg_rating = sum(book["ratings"]) / len(book["ratings"])
                book["avg_rating"] = avg_rating
                print(f"Thanks for your feedback, {user_name}! Current average rating for this book is {avg_rating:.2f} stars.")
            else:
                print("You haven't borrowed this book yet. Ratings can be given only after borrowing.")
        else:
            print("The book doesn't exist.")


    def add_user(self, name):
        if name not in self.users:
            self.users[name] = {
                'borrowed_books': [],
                'history': [],
                'ratings': {}
            }
        else:
            print(f"User {name} already exists!")

    def enhanced_search(self, query, search_type="general"):
        results = []
        for isbn, book in self.library_hash_table.items():
            if search_type == "title" and query in book["title"]:
                results.append(book)
            elif search_type == "author" and query in book["author"]:
                results.append(book)
            elif search_type == "general" and (query in book["title"] or query in book["author"]):
                results.append(book)
        return results

def main():
    system = LibraryManagementSystem()
    
    while True:
        print("Welcome to Oak Brook Public Library - Kids Section Management!")
        print("\nPlease choose from the following options:")
        print("1. Add a New Book to the Library")
        print("2. Search for a Book by Title or Author")
        print("3. Borrow a Book from the Library")
        print("4. Return a Borrowed Book")
        print("5. Renew a Book")
        print("6. Reserve a Book")
        print("7. Create a User Profile")
        print("8. Rate a Book")
        print("9. Enhanced Book Search")
        print("10. Exit the System")
        
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            print(system.add_book())
        elif choice == 2:
            books = system.search_book()
            if not books:
                print("No matching books found!")
            else:
                print("\nSearch Results:")
                for book in books:
                    avg_rating = book['avg_rating']
                    avg_rating_str = f"{avg_rating:.2f} stars" if isinstance(avg_rating, float) else "No ratings yet"
                    print(f"Title: {book['title']}, Author: {book['author']}, Publication Year: {book['publication_year']}, Status: {book['status']}, Rating: {avg_rating_str}")
        elif choice == 3:
            print(system.checkout_book())
        elif choice == 4:
            print(system.return_book())
        elif choice == 5:
            print(system.renew_book())
        elif choice == 6:
            print(system.reserve_book())
        elif choice == 7:
            user_name = input("Enter your name to create a user profile: ")
            system.add_user(user_name)
        elif choice == 8:
            isbn = input("Enter ISBN of the book you want to rate: ")
            user_name = input("Enter your name: ")
            rating = int(input("Give a rating (1 to 5 stars): "))
            if 1 <= rating <= 5:
                system.rate_book(isbn, user_name, rating)
            else:
                print("Invalid rating. Please provide a rating between 1 and 5 stars.")
        elif choice == 9:
            query = input("Enter title, author, or keyword for enhanced search: ")
            search_type = input("Search by title, author, or general? ").lower()
            books = system.enhanced_search(query, search_type)
            for book in books:
                avg_rating = book.get('avg_rating', 'No ratings yet')
                print(f"Title: {book['title']}, Author: {book['author']}, Avg Rating: {avg_rating}")
        elif choice == 10:
            print("Thank you for using the Oak Brook Public Library - Kids Section Management System!")
            break
        else:
            print("Invalid option selected. Please try again.")

if __name__ == "__main__":
    main()
