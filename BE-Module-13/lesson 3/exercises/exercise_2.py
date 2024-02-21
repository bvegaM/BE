class Book:
    def __init__(self, title, author, genre, isbn, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.quantity = quantity

class Node:
    def __init__(self, book):
        self.book = book
        self.next = None

class InventoryManager:
    def __init__(self):
        self.head = None

    def add_book(self, title, author, genre, isbn, quantity):
        new_book = Book(title, author, genre, isbn, quantity)
        new_node = Node(new_book)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_book(self, isbn):
        if not self.head:
            print("Inventory is empty.")
            return
        if self.head.book.isbn == isbn:
            self.head = self.head.next
            return
        prev = None
        current = self.head
        while current:
            if current.book.isbn == isbn:
                prev.next = current.next
                return
            prev = current
            current = current.next
        print("Book with ISBN {} not found in inventory.".format(isbn))

    def display_inventory(self):
        if not self.head:
            print("Inventory is empty.")
            return
        current = self.head
        print("Inventory:")
        while current:
            book = current.book
            print("Title: {}, Author: {}, Genre: {}, ISBN: {}, Quantity: {}".format(book.title, book.author, book.genre, book.isbn, book.quantity))
            current = current.next

# Usage Example:
inventory_manager = InventoryManager()

# Add books to the inventory
inventory_manager.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", "9780743273565", 10)
inventory_manager.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction", "9780061120084", 15)
inventory_manager.add_book("1984", "George Orwell", "Dystopian", "9780451524935", 12)

# Remove a book from the inventory
inventory_manager.remove_book("9780743273565")

# Display the current inventory
inventory_manager.display_inventory()