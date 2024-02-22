import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


# Array Implementation
def array_insertion(n):
    array = []
    for i in range(n):
        array.insert(0, i)

# Measure time for linked list insertion
def linked_list_insertion(n):
    linked_list = LinkedList()
    for i in range(n):
        linked_list.append(i)

# Measure time for array insertion
start_time = time.time()
array_insertion(100000)
end_time = time.time()
print("Time taken for array insertion:", end_time - start_time)

# Measure time for linked list insertion
start_time = time.time()
linked_list_insertion(100000)
end_time = time.time()
print("Time taken for linked list insertion:", end_time - start_time)