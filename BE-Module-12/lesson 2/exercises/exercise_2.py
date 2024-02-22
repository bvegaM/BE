import time

# Step 1: Create an empty list to store shopping items
shopping_list = []

# Step 2: Add item to the shopping list
def add_item(item):
    start_time = time.time()  # Start time for adding item
    shopping_list.append(item)
    end_time = time.time()  # End time for adding item
    add_time = end_time - start_time
    print(f"Item '{item}' added to the shopping list in {add_time:.7f} seconds.")

# Step 3: View the shopping list
def view_list():
    start_time = time.time()  # Start time for viewing list
    print("Shopping List:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")
    end_time = time.time()  # End time for viewing list
    view_time = end_time - start_time
    print(f"Viewing shopping list completed in {view_time:.7f} seconds.")

# Step 4: Mark item as purchased
def mark_as_purchased(index):
    start_time = time.time()  # Start time for marking item
    if 1 <= index <= len(shopping_list):
        shopping_list[index - 1] += " (Purchased)"
        print(f"Item '{shopping_list[index - 1]}' marked as purchased.")
    else:
        print("Invalid index. Please enter a valid index.")
    end_time = time.time()  # End time for marking item
    mark_time = end_time - start_time
    print(f"Marking item completed in {mark_time:.7f} seconds.")

# Step 5: Remove item from the shopping list
def remove_item(index):
    start_time = time.time()  # Start time for removing item
    if 1 <= index <= len(shopping_list):
        removed_item = shopping_list.pop(index - 1)
        print(f"Item '{removed_item}' removed from the shopping list.")
    else:
        print("Invalid index. Please enter a valid index.")
    end_time = time.time()  # End time for removing item
    remove_time = end_time - start_time
    print(f"Removing item completed in {remove_time:.7f} seconds.")

# Test the implementation
add_item('Apples')
add_item('Bananas')
add_item('Milk')
view_list()

mark_as_purchased(2)
remove_item(1)

view_list()