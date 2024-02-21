class TicketStack:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        """Adds a ticket to the top of the stack."""
        self.tickets.append(ticket)

    def remove_ticket(self):
        """Removes and returns the last ticket from the stack."""
        if not self.is_empty():
            return self.tickets.pop()

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.tickets) == 0

    def size(self):
        """Returns the number of tickets in the stack."""
        return len(self.tickets)

    def display_tickets(self):
        """Displays all tickets currently in the stack."""
        if self.is_empty():
            print("No tickets in the stack.")
        else:
            print("Tickets in the stack:")
            for ticket in self.tickets:
                print(f"- Ticket ID: {ticket['id']}, Priority: {ticket['priority']}, Description: {ticket['description']}")

# Example usage:
ticket_stack = TicketStack()

# Add tickets to the stack
ticket_stack.add_ticket({"id": 1, "priority": "High", "description": "Website is down"})
ticket_stack.add_ticket({"id": 2, "priority": "Medium", "description": "Can't login to account"})
ticket_stack.add_ticket({"id": 3, "priority": "Low", "description": "Need assistance with settings"})

# Display tickets in the stack
ticket_stack.display_tickets()

# Remove a ticket from the stack
removed_ticket = ticket_stack.remove_ticket()
print(f"Removed ticket: Ticket ID {removed_ticket['id']}")

# Display updated list of tickets in the stack
ticket_stack.display_tickets()