class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_kth_node(head, k):
    if not head:
        return None

    # Find the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Check if k is within the range of the linked list
    if k < 1 or k > length:
        return "Invalid value of k"

    # If k is the first or last node, no swapping needed
    if k == 1 or k == length:
        return head

    # Find the kth node from the beginning
    prev_k_from_beginning = None
    current = head
    for _ in range(k - 1):
        prev_k_from_beginning = current
        current = current.next

    # Find the kth node from the end
    prev_k_from_end = None
    current = head
    for _ in range(length - k):
        prev_k_from_end = current
        current = current.next

    # Swap the values of the kth nodes
    prev_k_from_beginning.val, prev_k_from_end.val = prev_k_from_end.val, prev_k_from_beginning.val

    return head

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original linked list:")
print_linked_list(head)

k = 2
head = swap_kth_node(head, k)

print(f"After swapping {k}th node from both ends:")
print_linked_list(head)
