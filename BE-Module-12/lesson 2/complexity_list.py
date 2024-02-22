import time

# Step 1: Create a list to represent a stone chest with a large number of stones
stone_chest = [f"stone_{i}" for i in range(1, 1000000)]

# Step 2: Measure the execution time of accessing the last stone
start_time = time.time()
_ = stone_chest[-1]  # Accessing the last stone
end_time = time.time()
access_time = end_time - start_time
print("Time taken to access the last stone:", access_time)

# Step 3: Measure the execution time of inserting a stone at the end
start_time = time.time()
stone_chest.append(f"stone_{len(stone_chest) + 1}")  # Inserting a stone at the end
end_time = time.time()
insert_time = end_time - start_time
print("Time taken to insert a stone at the end:", insert_time)

# Step 4: Measure the execution time of inserting a stone at the beginning
start_time = time.time()
stone_chest.insert(0, "stone_0")  # Inserting a stone at the beginning
end_time = time.time()
insert_beginning_time = end_time - start_time
print("Time taken to insert a stone at the beginning:", insert_beginning_time)

# Step 5: Measure the execution time of deleting a stone from the middle
start_time = time.time()
del stone_chest[len(stone_chest)//2]  # Deleting a stone from the middle
end_time = time.time()
delete_time = end_time - start_time
print("Time taken to delete a stone from the middle:", delete_time)

# Step 6: Measure the execution time of sorting the list
start_time = time.time()
stone_chest.sort()  # Sorting the list
end_time = time.time()
sort_time = end_time - start_time
print("Time taken to sort the list:", sort_time)