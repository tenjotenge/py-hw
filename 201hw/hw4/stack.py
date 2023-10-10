class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)
    
    def element_at_index(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            raise IndexError("index out of range")

# Example usage:
my_stack = Stack()

# Push elements onto the stack
print("Pushing first six prime numbers onto the stack.")
my_stack.push(2)
my_stack.push(3)
my_stack.push(5)
my_stack.push(7)
my_stack.push(11)
my_stack.push(13)

# Check if the stack is empty
print("Is the stack empty?", my_stack.is_empty())
print("Stack size:", my_stack.size())

# Get the top element (peek)
print("Top element:", my_stack.peek())

index = 4
try:
    element = my_stack.element_at_index(index)
    print(f"Element at index {index}: {element}")
except IndexError as e:
    print(e)


# Pop elements from the stack
print("Popping elements:")
while not my_stack.is_empty():
    print(my_stack.pop())

# Check the stack size
print("Stack size:", my_stack.size())
