import timeit
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_time(sort_func, arr):
    return timeit.timeit(lambda: sort_func(arr.copy()), number=10)

def generate_random_array(size):
    return random.sample(range(1, size * 10), size)

def compare_sorting_algorithms():
    sizes = [1000, 5000, 10000]  # Different sizes of input

    print("Size\tBubble Sort\tMerge Sort\tQuick Sort\tTimsort")
    for size in sizes:
        random_array = generate_random_array(size)
        bubble_time = measure_time(bubble_sort, random_array)
        merge_time = measure_time(merge_sort, random_array)
        quick_time = measure_time(quick_sort, random_array)
        timsort_time = timeit.timeit(lambda: sorted(random_array.copy()), number=10)
        print(f"{size}\t{bubble_time:.6f}\t{merge_time:.6f}\t{quick_time:.6f}\t{timsort_time:.6f}")


compare_sorting_algorithms()