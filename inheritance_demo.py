import unittest

class Collection:
    def __init__(self):
        self._items = []

    def add(self, item):
        pass

    def remove(self):
        pass

    def display(self):
        print(self._items)
    
    def __len__(self):
        return len(self._items)

class Stack(Collection):
    def add(self, item):
        self._items.append(item)

    def remove(self):
        if self._items:
            return self._items.pop()
        else:
            print("Stack is empty")
            return None

    def display(self):
        print("Stack:", self._items)

class Queue(Collection):
    def add(self, item):
        self._items.append(item)

    def remove(self):
        if self._items:
            return self._items.pop(0)
        else:
            print("Queue is empty")
            return None

    def display(self):
        print("Queue:", self._items)
    
    
class Deque(Collection):
    def add_front(self, item):
        self._items.insert(0, item)

    def add_rear(self, item):
        self._items.append(item)

    def remove_front(self):
        if self._items:
            return self._items.pop(0)
        else:
            print("Deque is empty from front")
            return None

    def remove_rear(self):
        if self._items:
            return self._items.pop()
        else:
            print("Deque is empty from rear")
            return None

    def display(self):
        print("Deque:", self._items)
        

class CircularQueue(Collection):
    def __init__(self, max_size):
        super().__init__()
        self._max_size = max_size
        self._front = 0
        self._rear = -1

    def add(self, item):
        if len(self._items) < self._max_size:
            self._rear = (self._rear + 1) % self._max_size
            self._items.insert(self._rear, item)
        else:
            print("Circular Queue is full")

    def remove(self):
        if self._items:
            item = self._items.pop(self._front)
            self._rear = (self._rear - 1) % self._max_size
            return item
        else:
            print("Circular Queue is empty")
            return None

    def display(self):
        print("Circular Queue:", self._items)
        
    
class PriorityQueue(Collection):
    def add(self, item):
        self._items.append(item)
        self._items.sort(reverse=True)  # Assume higher priority items are at the front

    def remove(self):
        if self._items:
            return self._items.pop(0)
        else:
            print("Priority Queue is empty")
            return None

    def display(self):
        print("Priority Queue:", self._items)
        
    
class DoubleEndedQueue(Collection):
    def add_front(self, item):
        self._items.insert(0, item)

    def add_rear(self, item):
        self._items.append(item)

    def remove_front(self):
        if self._items:
            return self._items.pop(0)
        else:
            print("Double-Ended Queue is empty from front")
            return None

    def remove_rear(self):
        if self._items:
            return self._items.pop()
        else:
            print("Double-Ended Queue is empty from rear")
            return None

    def display(self):
        print("Double-Ended Queue:", self._items)
        
# To demonstrate Multiple Inheritence:
class StackDeque(Stack, Deque):
    def __init__(self):
        # Call constructors of both parent classes
        Stack.__init__(self)
        Deque.__init__(self)

    def add_front(self, item):
        # Call method from Deque class
        Deque.add_front(self, item)

    def add_rear(self, item):
        # Call method from Deque class
        Deque.add_rear(self, item)

    def remove_front(self):
        # Call method from Deque class
        return Deque.remove_front(self)

    def remove_rear(self):
        # Call method from Deque class
        return Deque.remove_rear(self)

    def display(self):
        # Call method from Stack class
        Stack.display(self)



# Unit tests:

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.add(1)
        self.stack.add(2)

    def test_add(self):
        self.stack.add(3)
        self.assertEqual(len(self.stack), 3)

    def test_remove(self):
        removed_item = self.stack.remove()
        self.assertEqual(removed_item, 2)
        self.assertEqual(len(self.stack), 1)


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.queue.add(1)
        self.queue.add(2)

    def test_add(self):
        self.queue.add(3)
        self.assertEqual(len(self.queue), 3)

    def test_remove(self):
        removed_item = self.queue.remove()
        self.assertEqual(removed_item, 1)
        self.assertEqual(len(self.queue), 1)


class TestDeque(unittest.TestCase):
    def setUp(self):
        self.deque = Deque()
        self.deque.add_front(1)
        self.deque.add_rear(2)

    def test_add_front(self):
        self.deque.add_front(3)
        self.assertEqual(len(self.deque), 3)

    def test_add_rear(self):
        self.deque.add_rear(4)
        self.assertEqual(len(self.deque), 3)

    def test_remove_front(self):
        removed_item = self.deque.remove_front()
        self.assertEqual(removed_item, 1)
        self.assertEqual(len(self.deque), 1)

    def test_remove_rear(self):
        removed_item = self.deque.remove_rear()
        self.assertEqual(removed_item, 2)
        self.assertEqual(len(self.deque), 1)


# Add more test cases for CircularQueue, PriorityQueue, DoubleEndedQueue if needed

if __name__ == '__main__':
    unittest.main()



    # Example usage:
    stack = Stack()
    stack.add(1)
    stack.add(9)
    stack.add(2)
    stack.display()  # Output: Stack: [1, 9, 2]
    stack.remove()   
    stack.display()  # Output: Stack: [1, 9]
    print(len(stack)) # Output: 2
    
    queue = Queue()
    queue.add(1)
    queue.add(9)
    queue.add(2)
    queue.display()  # Output: Queue: [1, 9, 2]
    queue.remove()   
    queue.display()  # Output: Queue: [9, 2]
    
    deque = Deque()
    deque.add_front(1)
    deque.add_rear(2)
    deque.display()           # Output: Deque: [1, 2]
    deque.remove_front()      
    deque.remove_rear()       
    deque.display()           # Output: Deque: []
    
    
    circular_queue = CircularQueue(max_size=5)
    circular_queue.add(1)
    circular_queue.add(9)
    circular_queue.add(2)
    circular_queue.add(12)
    circular_queue.display()  # Output: Circular Queue: [1, 9, 2, 12]
    circular_queue.add(3)
    circular_queue.add(4)     # Output: Circular Queue is full
    circular_queue.display()  # Output: Circular Queue: [1, 9, 2, 12, 3]
    print(len(circular_queue)) # Output: 5
    circular_queue.remove()   
    circular_queue.display()  # Output: Circular Queue: [9, 2, 12, 3]
    circular_queue.remove()   
    circular_queue.display()  # Output: Circular Queue: [2, 12, 3]
    
    
    priority_queue = PriorityQueue()
    priority_queue.add(5)
    priority_queue.add(1)
    priority_queue.add(2)
    priority_queue.add(9)
    priority_queue.display()  # Output: Priority Queue: [9, 5, 2, 1]
    priority_queue.remove()   
    priority_queue.display()  # Output: Priority Queue: [5, 2, 1]
    
    double_ended_queue = DoubleEndedQueue()
    double_ended_queue.add_front(1)
    double_ended_queue.add_rear(2)
    double_ended_queue.display()           # Output: Double-Ended Queue: [1, 2]
    double_ended_queue.remove_front()      
    double_ended_queue.remove_rear()       
    double_ended_queue.display()           # Output: Double-Ended Queue: []
    
    stack_deque = StackDeque()
    stack_deque.add(1)
    stack_deque.add(2)
    stack_deque.add_front(3)
    stack_deque.add_rear(4)
    stack_deque.add_front(5)
    stack_deque.add(6)
    stack_deque.display()           # Output: Stack: [5, 3, 1, 2, 4, 6]
    print(len(stack_deque))         # Output: 6
    stack_deque.remove()            # Removes from Stack
    stack_deque.remove_front()      # Removes from Deque
    stack_deque.remove_rear()       # Removes from Deque
    stack_deque.display()           # Output: Stack: [3, 1, 2]
    print(len(stack_deque))         # Output: 3
