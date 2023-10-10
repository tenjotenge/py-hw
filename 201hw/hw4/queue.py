class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("front from empty queue")

    def size(self):
        return len(self.items)

    def element_at_index(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            raise IndexError("index out of range")

# Example usage for the Queue class:
my_queue = Queue()

# Enqueue elements into the queue
print("Enqueuing first six prime numbers into the queue.")
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(5)
my_queue.enqueue(7)
my_queue.enqueue(11)
my_queue.enqueue(13)

# Check if the queue is empty
print("Is the queue empty?", my_queue.is_empty())
print("Queue size:", my_queue.size())

# Get the front element
print("Front element:", my_queue.front())

index = 4
try:
    element = my_queue.element_at_index(index)
    print(f"Element at index {index}: {element}")
except IndexError as e:
    print(e)

# Dequeue elements from the queue
print("Dequeuing elements:")
while not my_queue.is_empty():
    print(my_queue.dequeue())

# Check the queue size
print("Queue size:", my_queue.size())
