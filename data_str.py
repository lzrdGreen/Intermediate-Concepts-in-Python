from collections import deque, Counter, OrderedDict, namedtuple
import heapq
import networkx as nx
import matplotlib.pyplot as plt

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


# Define a named tuple 'Point' with fields 'x' and 'y'
Point = namedtuple('Point', ['x', 'y'])

# Create a Point object
p = Point(1, 2)

# Access fields by name
print(p.x)  # Output: 1
print(p.y)  # Output: 2

# Example of using sets
my_set = set()  # Create an empty set
my_set.add(1)   # Add elements to the set
my_set.add(2)
my_set.add(3)
my_set.add(1)   # Adding duplicate element has no effect
print("Set:", my_set)  # Output: Set: {1, 2, 3}

# Example of set operations
other_set = {2, 3, 4}
union_set = my_set.union(other_set)
intersection_set = my_set.intersection(other_set)
difference_set = my_set.difference(other_set)
print("Union:", union_set)            # Output: Union: {1, 2, 3, 4}
print("Intersection:", intersection_set)  # Output: Intersection: {2, 3}
print("Difference:", difference_set)  # Output: Difference: {1}

# Example of using frozensets
my_frozenset = frozenset({1, 2, 3})  # Create a frozenset
print("Frozenset:", my_frozenset)   # Output: Frozenset: frozenset({1, 2, 3})

# As frozensets are immutable, they can be used as dictionary keys:
my_dict = {my_frozenset: "value"}
print("Dictionary:", my_dict)  # Output: Dictionary: {frozenset({1, 2, 3}): 'value'}

# As frozensets are immutable, you can't add new elements
# Uncomment the following line, it would raise an AttributeError: 'frozenset' object has no attribute 'add'
# my_frozenset.add(12)

# Let's draw a very simple graph, a triangle with nodes 1,2,and 3
# Create an empty graph
G1 = nx.Graph()

# Add nodes
G1.add_node(1)
G1.add_nodes_from([2, 3])

# Add edges
G1.add_edge(1, 2)
G1.add_edges_from([(1, 3), (2, 3)])

# Visualize the graph
nx.draw(G1, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()


# Now let's create a weighted graph and find the shortest path in it:
# Create a weighted graph
G2 = nx.Graph()
G2.add_edge('A', 'B', weight=4)
G2.add_edge('A', 'C', weight=2)
G2.add_edge('B', 'C', weight=5)
G2.add_edge('B', 'D', weight=10)
G2.add_edge('C', 'D', weight=3)
G2.add_edge('D', 'E', weight=7)

# Draw the graph
pos = nx.spring_layout(G2)  # Define layout for nodes
nx.draw(G2, pos, with_labels=True, node_color='lightblue', font_weight='bold')  # Draw nodes
edge_labels = nx.get_edge_attributes(G2, 'weight')
nx.draw_networkx_edge_labels(G2, pos, edge_labels=edge_labels)  # Draw edge labels
plt.show()

# Find the shortest path from node 'A' to node 'E' using Dijkstra's Algorithm
shortest_path = nx.dijkstra_path(G2, 'A', 'E', weight='weight')

print("Shortest path from 'A' to 'E':", shortest_path)  # Output: Shortest path from 'A' to 'E': ['A', 'C', 'D', 'E']

# BFS, breadth-first search using a queue


def bfs(graph, start):
    visited = set()            # Set to keep track of visited nodes
    queue = deque([start])     # Initialize queue with the starting node

    while queue:               # While the queue is not empty
        node = queue.popleft() # Dequeue a node from the front of the queue
        if node not in visited:
            print(node)        # Process the dequeued node (in this example, print it)
            visited.add(node)  # Mark the node as visited

            # Enqueue all unvisited adjacent nodes of the dequeued node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

print("BFS traversal starting from node 'A':")
bfs(graph, 'A')

# Binary search trees for searching and sorting

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal_recursive(self.root, result)
        return result

    def _in_order_traversal_recursive(self, node, result):
        if node:
            self._in_order_traversal_recursive(node.left, result)
            result.append(node.val)
            self._in_order_traversal_recursive(node.right, result)
            
    def search(self, val):
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node, val):
        if node is None:
            return False
        elif node.val == val:
            return True
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)




# Example usage:
bst = BinarySearchTree()
numbers = [5, 3, 8, 1, 7, 10, 6]

# Insert elements into the binary search tree
for num in numbers:
    bst.insert(num)

# Search for specific elements
print("Is 7 present in the tree?", bst.search(7))  # Output: Is 7 present in the tree? True
print("Is 4 present in the tree?", bst.search(4))  # Output: Is 4 present in the tree? False


# Example usage:
bst1 = BinarySearchTree()
numbers = [5, 3, 8, 1, 7, 10, 6, 3, 33]

# Insert elements into the binary search tree
for num in numbers:
    bst1.insert(num)

# Perform in-order traversal to retrieve sorted elements
sorted_numbers = bst1.in_order_traversal()
print("Sorted numbers:", sorted_numbers)




# Create a heap
# Or rather manipulate a list as a priority queue
# Example list
my_list = [3, 1, 4, 1, 5, 9, 2, 6]

# Convert the list into a heap with heapify method
heapq.heapify(my_list)

print("Heapified list:", my_list)  # Output: Heapified list: [1, 1, 2, 6, 5, 9, 4, 3]

# Push an element onto the heap
heapq.heappush(my_list, 7)

print("After pushing 7:", my_list)  # Output: After pushing 7: [1, 1, 2, 6, 5, 9, 4, 3, 7]

# Pop the smallest element from the heap
smallest = heapq.heappop(my_list)

print("Smallest element:", smallest)  # Output: Smallest element: 1
print("After popping smallest:", my_list)  # Output: After popping smallest: [1, 3, 2, 6, 5, 9, 4, 7]
