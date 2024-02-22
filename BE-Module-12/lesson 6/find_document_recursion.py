def find_document(folder):
    for item in folder:
        if item == "document.txt":  # Base case: Found the document
            return "Found it!"
        elif isinstance(item, list):  # Recursive case: It's a folder
            result = find_document(item)  # Continue searching inside the folder
            if result:
                return result
    return "Document not found"  # Base case: Reached the end of the folder without finding the document

# Example usage:
file_system = ["folder1", ["subfolder", "document.txt"], "folder2"]
print(find_document(file_system))