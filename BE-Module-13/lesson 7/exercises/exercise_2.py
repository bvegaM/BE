class PersonNode:
    def __init__(self, name, gender, relation=None):
        self.name = name
        self.gender = gender
        self.relation = relation
        self.children = []

class FamilyTree:
    def __init__(self):
        self.root = None

    def add_family_member(self, name, gender, parent_name=None, relation=None):
        person = PersonNode(name, gender, relation)
        if parent_name is None:
            if self.root is None:
                self.root = person
            else:
                print("Cannot add root family member without specifying a parent.")
        else:
            parent = self._find_person(self.root, parent_name)
            if parent:
                parent.children.append(person)
            else:
                print(f"Parent '{parent_name}' not found in the family tree. Cannot add child '{name}'.")

    def _find_person(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        for child in node.children:
            found_person = self._find_person(child, name)
            if found_person:
                return found_person
        return None

    def print_family_tree(self):
        self._print_recursive(self.root, 0, True)

    def _print_recursive(self, node, depth, is_last):
        if node:
            print("    " * depth, end="")
            if is_last:
                print("└── ", end="")
            else:
                print("├── ", end="")
            print(f"{node.name} ({node.gender}) - {node.relation}")
            for i, child in enumerate(node.children):
                is_last_child = i == len(node.children) - 1
                self._print_recursive(child, depth + 1, is_last_child)

# Test the FamilyTree class
if __name__ == "__main__":
    family_tree = FamilyTree()

    # Add family members to the tree with their relations
    family_tree.add_family_member("John Doe", "Male", relation="Father")
    family_tree.add_family_member("Alice Doe", "Female", "John Doe", relation="Daughter")
    family_tree.add_family_member("Bob Doe", "Male", "Alice Doe", relation="Grandson")
    family_tree.add_family_member("Eva Doe", "Female", "John Doe", relation="Daughter")

    # Print the family tree
    print("Family Tree:")
    family_tree.print_family_tree()