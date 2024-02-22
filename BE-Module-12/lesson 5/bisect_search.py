import bisect

# Example usage:
sorted_list = [1, 2, 3, 7, 9]
target_element = 7
index = bisect.bisect_left(sorted_list, target_element)
if index < len(sorted_list) and sorted_list[index] == target_element:
    print(index)  # Output: 3 (index of the target element)
else:
    print(-1)  # If the target is not found