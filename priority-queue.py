import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item, priority):
        heapq.heappush(self.items, (priority, item))

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.items)[1]
        else:
            raise IndexError("dequeue from empty priority queue")

    def front_element(self):
        if not self.is_empty():
            return self.items[0][1]
        else:
            raise IndexError("front from empty priority queue")

    def size(self):
        return len(self.items)

# Example usage for the PriorityQueue class:
my_priority_queue = PriorityQueue()

# Enqueue elements into the priority queue
print("Enqueuing elements into the priority queue:")
my_priority_queue.enqueue("Task 1", 3)
print("Task 1: priority 3")
my_priority_queue.enqueue("Task 2", 1)
print("Task 2: priority 1")
my_priority_queue.enqueue("Task 3", 2)
print("Task 3: priority 2")

# Check if the priority queue is empty
print("Is the priority queue empty?", my_priority_queue.is_empty())
print("Priority Queue size:", my_priority_queue.size())

# Get the front element
print("Front element:", my_priority_queue.front_element())

# Dequeue elements from the priority queue
print("Dequeuing elements:")
while not my_priority_queue.is_empty():
    print(my_priority_queue.dequeue())

# Check the priority queue size
print("Priority Queue size:", my_priority_queue.size())
