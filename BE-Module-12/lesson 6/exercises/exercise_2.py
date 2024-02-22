def calculate_total_file_size(file_system):
    total_size = 0

    for item in file_system:
        if isinstance(item, int):  # Assuming item represents file size
            total_size += item
        elif isinstance(item, list):  # Assuming item represents a folder
            total_size += calculate_total_file_size(item)

    return total_size

# Example usage:
file_system = [
  [10, 20, 30],  # Folder 1 with files of sizes 10, 20, and 30
  [15, [25, 35]],  # Folder 2 with files of sizes 15, 25, and 35
  40,  # File 1 with size 40
  [45, [55, 65]],  # Folder 3 with files of sizes 45, 55, and 65
  70  # File 2 with size 70
]

print(calculate_total_file_size(file_system))  # Output: 345 (sum of all file sizes)