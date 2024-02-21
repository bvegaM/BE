def find_file(file_system, file_name):
    for item in file_system:
        if item == file_name:
            return f"Found {file_name}!"
        elif isinstance(item, list):
            result = find_file(item, file_name)
            if result:
                return result
    return f"{file_name} not found."

# Example usage:
file_system = ["folder1", ["subfolder", "report.pdf"], "folder2"]
print(find_file(file_system, "report.pdf"))  # Output: Found report.pdf!
print(find_file(file_system, "presentation.ppt"))  # Output: presentation.ppt not found.