class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Single_linked_list:
    def __init__(self):
        self.head = None 

    # ------------------- INSERT -------------------
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data, pos):
        new_node = Node(data)
        if pos == 0:   # insert at head
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        count = 0
        while temp and count < pos - 1:
            temp = temp.next
            count += 1
        if temp is None:
            print("Position out of range")
            return
        new_node.next = temp.next
        temp.next = new_node

    # ------------------- DELETE -------------------
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:  # only one node
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 0:
            self.head = self.head.next
            return
        temp = self.head
        count = 0
        while temp and count < pos - 1:
            temp = temp.next
            count += 1
        if temp is None or temp.next is None:
            print("Position out of range")
            return
        temp.next = temp.next.next

    # ------------------- SEARCH -------------------
    def search(self, key):
        temp = self.head
        pos = 0
        while temp:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1
        return -1

    # ------------------- UTILITY -------------------
    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def is_circular(self):
        if self.head is None:
            return False
        temp = self.head.next
        while temp is not None and temp != self.head:
            temp = temp.next
        return temp == self.head
    
    def make_circular(self):
        if self.head is None:
            return
        if self.is_circular():
            print("Already circular")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = self.head 

    # ------------------- DISPLAY -------------------
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def display_circular(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

sll = Single_linked_list()

# Insert elements
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_beginning(5)
sll.insert_at_position(15, 2)
sll.display()     # 5 -> 10 -> 15 -> 20 -> 30 -> None

# Delete elements
sll.delete_at_beginning()
sll.display()     # 10 -> 15 -> 20 -> 30 -> None

sll.delete_at_end()
sll.display()     # 10 -> 15 -> 20 -> None

sll.delete_at_position(1)
sll.display()     # 10 -> 20 -> None

# Reverse
sll.reverse()
sll.display()     # 20 -> 10 -> None

# Search
print("Found at index:", sll.search(20))  # Found at index: 0
print("Length:", sll.length())            # Length: 2

# Make circular and print
sll.make_circular()
sll.display_circular()  # 20 -> 10 -> (back to head)