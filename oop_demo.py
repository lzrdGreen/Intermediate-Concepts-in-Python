import heapq, unittest

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
    def __len__(self):
        return len(self._queue)


class TestPriorityQueue(unittest.TestCase):
    def test_push_pop(self):
        pq = PriorityQueue()
        pq.push('taskA', 3)
        pq.push('taskB', 1)
        pq.push('taskC', 2)
        pq.push('taskD', 1)
        
        self.assertEqual(len(pq), 4) # Length of the queue is 4
        self.assertEqual(pq.pop(), 'taskB')  # First item popped should be 'taskB'
        self.assertEqual(pq.pop(), 'taskD')  # Second item popped should be 'taskD'
        self.assertEqual(pq.pop(), 'taskC')  # Third item popped should be 'taskC'
        self.assertEqual(pq.pop(), 'taskA')  # Last item popped should be 'taskA'
        
    def test_empty_queue(self): # Edge case
        pq = PriorityQueue()
        self.assertRaises(IndexError, pq.pop)  # Attempting to pop from an empty queue should raise IndexError




# Example usage for MST with Prim's Algorithm
def prim_mst(graph):
    pq = PriorityQueue()
    visited = set()
    mst = []

    start_node = next(iter(graph))
    visited.add(start_node)
    for neighbor, weight in graph[start_node]:
        pq.push((start_node, neighbor, weight), weight)

    while pq:
        u, v, weight = pq.pop()
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for neighbor, edge_weight in graph[v]:
                if neighbor not in visited:
                    pq.push((v, neighbor, edge_weight), edge_weight)
    
    return mst


if __name__ == '__main__':
    unittest.main()


    # Example usage:
    pq = PriorityQueue()
    pq.push('taskA', 3)
    pq.push('taskB', 1)
    pq.push('taskC', 2)
    pq.push('taskD', 1)
    
    print(pq.pop())  # Output: 'taskB'
    print(pq.pop())  # Output: 'taskD'
    print(pq.pop())  # Output: 'taskC'
    
   # Graph representation
    graph = {
        'A': [('B', 2), ('D', 5)],
        'B': [('A', 2), ('C', 3), ('D', 3)],
        'C': [('B', 3), ('D', 1), ('E', 5)],
        'D': [('A', 5), ('B', 3), ('C', 1), ('E', 2)],
        'E': [('C', 5), ('D', 2)]
    }
    
    # Find the minimum spanning tree (MST) using Prim's algorithm
    mst = prim_mst(graph)
    
    # Print the minimum spanning tree
    print("Minimum Spanning Tree (MST):")
    for edge in mst:
        print(edge)