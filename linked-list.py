#linked list code

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

    # function to print all values in a linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# code to create, populate, and display a linked list 
# in the terminal using our two classes

# Create a linked list
my_linked_list = LinkedList()

# Add values to the linked list
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

# Display the values in the linked list
my_linked_list.display()
