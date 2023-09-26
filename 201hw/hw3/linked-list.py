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

    def remove_duplicates(self):
        if not self.head:
            return

        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def union(self, other_list):
        union_list = LinkedList()
        current = self.head

        while current:
            union_list.append(current.data)
            current = current.next

        current_other = other_list.head
        while current_other:
            if not union_list.contains(current_other.data):
                union_list.append(current_other.data)
            current_other = current_other.next

        return union_list

    def intersection(self, other_list):
        intersection_list = LinkedList()
        current = self.head

        while current:
            if other_list.contains(current.data):
                intersection_list.append(current.data)
            current = current.next

        return intersection_list

    def contains(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

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

# We will now create two separate linked lists, then create a third that exists 
# as the sum of the first two linked lists at each index.

print("Now creating linked list using the sum of two other linked lists to fill the data:")

# Create the first linked list
list1 = LinkedList()
print("Enter values for the first linked list (enter a non-integer to stop):")
while True:
    try:
        value = int(input())
        list1.append(value)
    except ValueError:
        break

# Create the second linked list
list2 = LinkedList()
print("Enter values for the second linked list (enter a non-integer to stop):")
while True:
    try:
        value = int(input())
        list2.append(value)
    except ValueError:
        break

# Display the first and second linked lists
print("First Linked List:")
list1.display()
print("Second Linked List:")
list2.display()

# Create the third linked list with sums
list3 = LinkedList()
current1 = list1.head
current2 = list2.head
while current1 and current2:
    sum_value = current1.data + current2.data
    list3.append(sum_value)
    current1 = current1.next
    current2 = current2.next

# Display the third linked list
print("Third Linked List (Sum of the First and Second Lists):")
list3.display()

# Create the fourth linked list (Union of List 1 and List 2)
list4 = list1.union(list2)
print("Fourth Linked List (Union of First and Second Lists):")
list4.display()

# Create the fifth linked list (Intersection of List 1 and List 2)
list5 = list1.intersection(list2)
print("Fifth Linked List (Intersection of First and Second Lists):")
list5.display()