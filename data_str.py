from collections import deque, Counter, OrderedDict

# Deques (double-ended queues) are optimized for fast appends and pops from both ends.
# They can be used to efficiently implement stacks, queues, etc
# create an instance and print it out
my_deque = deque([1, 22, -3, 40, 5])
print(list(my_deque)) # Output: [1, 22, -3, 40, 5]

# an example of stack implementation
class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def __str__(self):
        return str(list(self.stack))

    def __len__(self):
        return len(self.stack)

# an example of queue implementation
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(list(self.queue))

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(22)
queue.enqueue(3)

print(queue)        # Output: [1, 22, 3]
print(len(queue))   # Output: 3
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 22
print(queue.is_empty())  # Output: False
print(queue.dequeue())  # Output: 3
print(queue.is_empty())  # Output: True

# Example of stack usage:
stack = Stack()
stack.push(1)
stack.push(20)
stack.push(3)

print(stack.peek())  # Output: 3
print(stack)        # Output: [1, 20, 3]
print(len(stack))   # Output: 3
print(stack.pop())   # Output: 3
print(stack.pop())   # Output: 20
print(stack.is_empty())  # Output: False
print(stack.pop())   # Output: 1
print(stack.is_empty())  # Output: True
print(stack.peek())  # Output: None


# How to use Counters

# Create a Counter object
my_counter = Counter(['a', 'b', 'a', 'c', 'b', 'a', 'd'])

# Count occurrences of elements
print(my_counter)  # Output: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})

# Get the two most common elements
print(my_counter.most_common(2))  # Output: [('a', 3), ('b', 2)]

my_ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(my_ordered_dict) # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
my_ordered_dict['x'] =25
print(my_ordered_dict) # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3), ('x', 25)])
my_ordered_dict.pop('c')
print(my_ordered_dict) # Output: OrderedDict([('a', 1), ('b', 2), ('x', 25)])
my_ordered_dict['c'] = -99
print(my_ordered_dict) # Output: OrderedDict([('a', 1), ('b', 2), ('x', 25), ('c', -99)])



