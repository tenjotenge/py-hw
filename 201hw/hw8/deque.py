from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue_front(self, item):
        self.items.appendleft(item)

    def enqueue_rear(self, item):
        self.items.append(item)

    def dequeue_front(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("dequeue from empty deque")

    def dequeue_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("dequeue from empty deque")

    def front_element(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("front from empty deque")

    def rear_element(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("rear from empty deque")

    def size(self):
        return len(self.items)

# Example usage for the Deque class:
my_deque = Deque()

# Enqueue elements into the deque
print("Enqueuing elements into the deque:")
my_deque.enqueue_front(1)
my_deque.enqueue_front(2)
my_deque.enqueue_rear(3)
my_deque.enqueue_rear(4)

# Check if the deque is empty
print("Is the deque empty?", my_deque.is_empty())
print("Deque size:", my_deque.size())

# Get the front and rear elements
print("Front element:", my_deque.front_element())
print("Rear element:", my_deque.rear_element())

# Dequeue elements from the deque
print("Dequeuing elements from the front:")
while not my_deque.is_empty():
    print("Dequeuing front:", my_deque.dequeue_front())

# Check the deque size
print("Deque size:", my_deque.size())

# Enqueue more elements into the deque
print("Enqueuing more elements into the deque:")
my_deque.enqueue_front(5)
my_deque.enqueue_rear(6)

# Get the front and rear elements after enqueuing more elements
print("Front element:", my_deque.front_element())
print("Rear element:", my_deque.rear_element())

# Dequeue elements from the rear
print("Dequeuing elements from the rear:")
while not my_deque.is_empty():
    print("Dequeuing rear:", my_deque.dequeue_rear())

# Check the deque size after dequeuing from the rear
print("Deque size:", my_deque.size())
