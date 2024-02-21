class EmployeeNode:
    def __init__(self, name, emp_id, position):
        self.name = name
        self.emp_id = emp_id
        self.position = position
        self.left = None
        self.right = None

class OrganizationTree:
    def __init__(self):
        self.root = None

    def insert_employee(self, name, emp_id, position):
        if self.root is None:
            self.root = EmployeeNode(name, emp_id, position)
        else:
            self._insert_recursive(self.root, name, emp_id, position)

    def _insert_recursive(self, node, name, emp_id, position):
        if emp_id < node.emp_id:
            if node.left is None:
                node.left = EmployeeNode(name, emp_id, position)
            else:
                self._insert_recursive(node.left, name, emp_id, position)
        elif emp_id > node.emp_id:
            if node.right is None:
                node.right = EmployeeNode(name, emp_id, position)
            else:
                self._insert_recursive(node.right, name, emp_id, position)

    def print_organization_hierarchy(self):
        self._print_recursive(self.root, 0)

    def _print_recursive(self, node, depth):
        if node:
            self._print_recursive(node.right, depth + 1)
            print("    " * depth + f"{node.name} ({node.position})")
            self._print_recursive(node.left, depth + 1)

# Test the OrganizationTree class
if __name__ == "__main__":
    org_tree = OrganizationTree()

    # Insert employees into the tree
    org_tree.insert_employee("John Doe", 101, "CEO")
    org_tree.insert_employee("Jane Smith", 201, "CTO")
    org_tree.insert_employee("Alice Johnson", 151, "HR Manager")
    org_tree.insert_employee("Bob Williams", 401, "Software Engineer")
    org_tree.insert_employee("Emily Brown", 301, "Data Analyst")
    org_tree.insert_employee("Michael Davis", 501, "Marketing Manager")

    # Print the organizational hierarchy
    print("Organizational Hierarchy:")
    org_tree.print_organization_hierarchy()