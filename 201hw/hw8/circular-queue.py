class CircularQueue:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.front = self.rear = -1
        self.capacity = capacity

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("enqueue to full queue")
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        removed_item = self.items[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return removed_item

    def front_element(self):
        if not self.is_empty():
            return self.items[self.front]
        else:
            raise IndexError("front from empty queue")

    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.capacity - self.front + self.rear + 1

# Example usage for the CircularQueue class:
my_circular_queue = CircularQueue(5)

# Enqueue elements into the circular queue
print("Enqueuing elements into the circular queue:")
for i in range(1, 6):
    my_circular_queue.enqueue(i)
    print(f"Enqueued: {i}")

# Check if the circular queue is empty
print("Is the circular queue empty?", my_circular_queue.is_empty())
print("Circular Queue size:", my_circular_queue.size())

# Get the front element
print("Front element:", my_circular_queue.front_element())

# Dequeue elements from the circular queue
print("Dequeuing elements:")
while not my_circular_queue.is_empty():
    print(my_circular_queue.dequeue())

# Check the circular queue size
print("Circular Queue size:", my_circular_queue.size())
