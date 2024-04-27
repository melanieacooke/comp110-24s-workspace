class Node:
    """An item in a singly-linked list."""
    data: int
    next: Node | None
 
    def __init__(self, data: int, next: Node | None):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next
 
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"

    def head(self) -> int:
        """Return the data attribute of the head of the list."""
        return self.data

    def tail(self) -> Node | None:
        """Return the linked list starting from the node after the current node."""
        return self.next

    def last(self) -> int:
        """Return the data of the last element in the linked list."""
        current = self
        while current.next is not None:
            current = current.next
        return current.data