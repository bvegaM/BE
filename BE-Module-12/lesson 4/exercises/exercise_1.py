class CommentQueue:
    def __init__(self):
        self.comments = []

    def post_comment(self, comment):
        """Adds a comment to the end of the queue."""
        self.comments.append(comment)

    def delete_comment(self):
        """Removes and returns the first comment from the queue."""
        if not self.is_empty():
            return self.comments.pop(0)

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.comments) == 0

    def size(self):
        """Returns the number of comments in the queue."""
        return len(self.comments)

    def display_comments(self):
        """Displays all comments currently in the queue."""
        if self.is_empty():
            print("No comments in the queue.")
        else:
            print("Comments in the queue:")
            for comment in self.comments:
                print(f"- {comment['timestamp']} by {comment['username']}: {comment['text']}")

# Example usage:
comment_queue = CommentQueue()

# Post comments to the queue
comment_queue.post_comment({"id": 1, "timestamp": "2024-02-15 10:00:00", "username": "user1", "text": "Great post!"})
comment_queue.post_comment({"id": 2, "timestamp": "2024-02-15 10:15:00", "username": "user2", "text": "I enjoyed reading this."})
comment_queue.post_comment({"id": 3, "timestamp": "2024-02-15 10:30:00", "username": "user3", "text": "Thanks for sharing."})

# Display comments in the queue
comment_queue.display_comments()

# Delete a comment from the queue
deleted_comment = comment_queue.delete_comment()
print(f"Deleted comment: {deleted_comment['text']}")

# Display updated list of comments in the queue
comment_queue.display_comments()