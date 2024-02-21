# queue.py

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Adds an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Removes and returns the first item from the queue."""
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Returns the number of items in the queue."""
        return len(self.items)
