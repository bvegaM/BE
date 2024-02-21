import time
import random

# Step 1: Create a stone chest (dictionary) with a large number of stones
stone_chest = {'stone_' + str(i): random.randint(1, 1000) for i in range(1000000)}

# Step 2: Measure the execution time of accessing the last stone
start_time = time.time()
_ = stone_chest['stone_999999']  # Accessing the last stone
end_time = time.time()
access_time = end_time - start_time
print("Time taken to access the last stone:", access_time)

# Step 3: Measure the execution time of inserting a stone
start_time = time.time()
stone_chest['new_stone'] = random.randint(1, 1000)  # Inserting a stone
end_time = time.time()
insert_time = end_time - start_time
print("Time taken to insert a stone:", insert_time)

# Step 4: Measure the execution time of deleting a stone
start_time = time.time()
del stone_chest['stone_500000']  # Deleting a stone
end_time = time.time()
delete_time = end_time - start_time
print("Time taken to delete a stone:", delete_time)

# Step 5: Measure the execution time of iterating over all stones
start_time = time.time()
for key, value in stone_chest.items():
    pass
end_time = time.time()
iteration_time = end_time - start_time
print("Time taken to iterate over all stones:", iteration_time)