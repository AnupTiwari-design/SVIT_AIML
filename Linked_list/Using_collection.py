from collections import deque

# Create linked list
linked_list = deque()

# Insert elements (like insert at end)
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
print("Linked List:", list(linked_list))

# Insert at beginning
linked_list.appendleft(5)
print("After appendleft:", list(linked_list))

# Remove from end
linked_list.pop()
print("After pop:", list(linked_list))

# Remove from beginning
linked_list.popleft()
print("After popleft:", list(linked_list))

# Size
print("Size:", len(linked_list))

# Check if empty
print("Is Empty:", len(linked_list) == 0)