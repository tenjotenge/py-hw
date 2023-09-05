# Basic linked list code

# class for nodes which will exist as object in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class for the linked list object
class LinkedList:
    def __init__(self):
        self.head = None

    # function that allows you to add values to linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # function to insert an element into the list at any given index
    def insert(self, position, data):
        if position < 0:
            print("Invalid position. Position should be non-negative.")
            return
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        current_position = 0
        while current_position < position - 1 and current.next:
            current = current.next
            current_position += 1
        if current_position == position - 1:
            new_node.next = current.next
            current.next = new_node
        else:
            print("Invalid position. Position exceeds the length of the list.")

    # function to print all values in a linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("End")

    # function to remove the head of the list
    def remove_first(self):
        if self.head:
            self.head = self.head.next

# Code to create, populate, and display a linked list 
# in the terminal using our two classes

# Create a linked list
my_linked_list = LinkedList()

# Add values to the linked list

while True:
    try:
        value = int(input("Enter a value (or any non-integer to stop): "))
        my_linked_list.append(value)
    except ValueError:
        break

# Display the values in the linked list
print("Now printing Linked List: 'End' will indicate the prior element was the last within the list.")
my_linked_list.display()

# Remove the first element
my_linked_list.remove_first()

# Display the values in the linked list after removal
print("Linked List after removing the first element:")
my_linked_list.display()

# Allow the user to insert a value at a specific position
try:
    position = int(input("Enter the position to insert (0 for head): "))
    insert_value = int(input("Enter the value to insert: "))
    my_linked_list.insert(position, insert_value)
except ValueError:
    print("Invalid input for position or value.")

# Display the values in the linked list after insertion
print("Linked List after insertion:")
my_linked_list.display()