import timeit
import random
import bisect

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def bisect_search(arr, target):
    index = bisect.bisect_left(arr, target)
    if index < len(arr) and arr[index] == target:
        return index
    return -1

# Function to generate a sorted list of random integers
def generate_sorted_list(size):
    return sorted(random.sample(range(1, 1000000), size))

# Function to measure execution time for linear search
def measure_linear_search(size):
    arr = generate_sorted_list(size)
    target = random.randint(1, 1000000)
    time = timeit.timeit(lambda: linear_search(arr, target), number=10)
    return time / 10  # Taking average of 10 runs

# Function to measure execution time for binary search
def measure_binary_search(size):
    arr = generate_sorted_list(size)
    target = random.randint(1, 1000000)
    time = timeit.timeit(lambda: binary_search(arr, target), number=10)
    return time / 10  # Taking average of 10 runs

# Function to measure execution time for bisect search
def measure_bisect_search(size):
    arr = generate_sorted_list(size)
    target = random.randint(1, 1000000)
    time = timeit.timeit(lambda: bisect_search(arr, target), number=10)
    return time / 10  # Taking average of 10 runs

# Main function to compare the performance of linear, binary, and bisect search
def compare_search_algorithms():
    sizes = [1000, 5000, 10000, 50000, 100000]  # Different sizes of input

    print("Size\tLinear Search\tBinary Search\tBisect Search")
    for size in sizes:
        linear_time = measure_linear_search(size)
        binary_time = measure_binary_search(size)
        bisect_time = measure_bisect_search(size)
        print(f"{size}\t{linear_time:.6f}\t\t{binary_time:.6f}\t\t{bisect_time:.6f}")

compare_search_algorithms()