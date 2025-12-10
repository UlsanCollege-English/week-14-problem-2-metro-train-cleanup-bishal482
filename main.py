class Node:
   

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def remove_cars(head, target):
    
    # Remove leading nodes with value == target
    while head is not None and head.value == target:
        head = head.next
    # Now head is either None or not target
    current = head
    prev = None
    while current is not None:
        if current.value == target:
            # Remove current node
            prev.next = current.next
            current = current.next
        else:
            prev = current
            current = current.next
    return head


if __name__ == "__main__":
    # Optional manual test
    # Example train: 1 -> 2 -> 2 -> 3, remove cars with ID 2
    n4 = Node(3)
    n3 = Node(2, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)

    new_head = remove_cars(n1, 2)
    curr = new_head
    while curr is not None:
        print(curr.value, end=" ")
        curr = curr.next
    print()
