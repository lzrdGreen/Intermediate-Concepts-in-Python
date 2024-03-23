# Intermediate-Concepts-in-Python
## Intermediate Concepts and Best Practices in Python
Basic syntax, data types, common in-built data structures (strings, lists, tuples, sets, dictionaries), control flow methods (loops, conditionals, and functions), or importing modules (*.py files) probably don’t need any special demonstration. 

More  advanced concepts like object-oriented programming (including classes, instances and methods, data abstraction, inheritance, encapsulation, polymorphism, discussion of the OOP vs functional programming, etc), exception handling, file handling,  lambda functions (especially in list comprehension and for pandas series), generators, regular expressions, maps, collections, decorators will be demonstrated in this repo. It is important to test software as it is developed. The most basic level is formed by unit tests.
### Generators
In Python, a [generator](https://docs.python.org/3/tutorial/classes.html#generators) is a function which returns a generator iterator. It produces a series of values which can be retrieved one at a time with next() function. It's a call-by-need evaluation strategy sometimes called lazy evaluation. It saves memory. Run gen.py to see how it works.

A good illustration of generator's memory efficiency are Fibonacci numbers. Fibonacci sequence is used sometimes to illustrate recursion but it doesn't work well as a straightforward recursion (fib_new = fib_current + fub_previous) quickly runs out of memory. A generator only keeps track of the last two Fibonacci numbers generated. 

Another (practical) example is a countdown timer. Each second you call the generator to yield a new value. Generating permutations (or combinations) of elements, random sampling or file processing in batches saves memory as permutations, samples or batches are produced on the fly. This helps in Machine Learning for data preprocessing or cleaning, image resizing/ cropping in face recognition systems, log file analysis, etc. Generators can be used to implement asynchronous programming patterns, enabling concurrent execution (e.g. real-time data sreaming) of tasks without the complexity of traditional threading or multiprocessing.

### Lambda functions
Lambda functions are anonymous functions (=functions without a name). They are defined using the lambda keyword and can take any number of arguments but can only have one expression. Lambda functions are used in situations where you need a small function for a short period of time and don't want to define a full-fledged function using the def keyword. (Please see a collection of simple examples in lambda_demo.py).

It makes sense to use a lambda function with iterables (such as lists, strings, tuples, dictionaries) in order to produce another iterable, e.g. to filter a list. If you sort a list of tuples, strings or dictionaries based on some parameter, use this parameter as a key. Using such key also helps if you need an element with the largest or smallest value of the parameter, say a person who gets the largest salary in your organisation. Some people say that list comprehension with anonymous functions looks particularly "pythonic". It's a matter of taste but sometimes applying lambda functions too freely may produce unexpected results (I mean this example: squared_numbers = [lambda x: x**2 for x in numbers]). Also avoid complicated (e.g., nested conditionals) lambda functions as they make the code difficult to read. As lambda functions are simple by definition, you probably don't need to create test cases for them, just print out the result and compare with your expectations.

You can use a lambda function to modify another function and to assign it to a variable. For instance, first, define a multiplier, then by passing the correct multiplication factor (2 or 3) create a doubler or a tripler.


It's useful to know that lambda functions can help with writing a simple code for data transformation in a pandas series (= a column in a data frame).

You may find this link useful: ["How to Use Python Lambda Functions"](https://realpython.com/python-lambda/)

### Data structures from collections, heapq, networkx and beyond
Python has 4 built-in data structures: lists, tuples, sets and dictionaries. They are all iterables (objects that can be iterated over with the help of a for loop). Another important iterable is an object called strings, they are not considered as data structures but rather a data type (an immutable sequence of characters). Sometimes strings along with float, integer and boolean variables are called primitive data structures.

These four data structures are so important and widely used that they are built in the language itself and optimised. They come with their own methods. Still you may need more advanced data structures (to store and organise your data) - some of them can be imported from existing libraries, others are user-defined. The choice of data structure depends on the requirements of your problem: which operations needs to be the most efficient - searching? sorting? insertion/ deletion? Understanding the strengths and weaknesses of the data structure you use is crucial.

**Queues:** first-in-first-out (FIFO) data structures useful in modelling waiting lines (=queues) and breadth-first search.

**Stacks:** last-in-first-out (LIFO) data structures useful for recursive algorithms and undo operations - visualise LIFO as a stack of plates.

**Graphs:** collections of nodes (vertices) and edges (links) that represent some kind of relationship between the objects represented by nodes. Graphs can represent chemical structures, social networks, help find the shortest path in route planning, etc. Graphs are very well studied in the graph theory and computer science. Even if you can't have an exact solution, quite often you can have an approximate algorithm which produces a reasonably good result (the travelling salesperson problem, TSP, is NP-hard but you have some algorithms which normally give you a route that is slightly worse than the optimal route). Graphs can be directed or undirected.

**Trees:** hierarchical data structures with parent-child relationships, often used for efficient searching and sorting. In graph theory a tree is an undirected graph in which any two nodes are connected by exactly one edge, and there are no cycles. In computer science a tree is also a graph (a directed acyclic graph - DAG) which has a root (a node without any parent), nodes (with a parent and children) and leaves (nodes without children). It looks like a flipped over tree. Binary trees are extremely often used.

There is a number of list-like data structure: arrays, numpy arrays, linked lists, circular linked lists, namedtuples - to name a few.

There are various dictionary-like structures: hash tables (in fact, a dictionary in Python is a kind of hash table under the hood), OrderedDict, etc

Some other data structures: heaps, priority queues, tries (= prefix trees), various probabilistic data structures (Bloom filters, Bayesian networks, Markov random fields). I am not going to discuss probabilistic data structures here as they are quite advanced.

All examples of implementation of data structures using libraries/ modules are presented in data_str.py.

If I couldn't find a suitable library to create a data structure discussed above, they are delayed until the next section about Python classes.

In data_str.py I use deque objects (from the collections module) to implement both **stacks** and **queues** with most important methods for them: push and pop new elements, view the element to be popped next without removing it (peek), print out the stack/ queue, find out its length.

By the way, another useful object in the library collections is **Counter**. It is not a data structure, of course , but I included an example of how to use Counter anyway.

In Python dictionaries are unordered collections of key-value pairs. You may need a dictionary-like structure which remembers the order in which its elements were added: **OrderedDict**, a dictionary subclass from the collections. It maintains the order of insertion, unlike regular/ built-in dictionaries which may reorder the elements for efficiency.

Now you need to install these modules:matplotlib, networkx.I recommend using: conda install networkx matplotlib (if you installed your Python using Miniconda or Anaconda).

First I create a simple graph G1, just as a demonstration how to use networkx module. The next graph G2 is used to show Dijkstra's algorithm, which finds the shortest path between nodes. The module has a built-in method for Graph() objects for this operation. You may wish to take a look at an implementation of the [Dijkstra's algorithm in Python](https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html) from scratch. An interesting thing about Dijkstra's algorithm is that it is "greedy", i.e. it builds the path by always going to the nearest next node.

Next I show how to use a queue, the data sructure we discussed at the beginning, for search, to be specific, for breadth-first search (BFS). Please note that I represent a graph as a dictionary: each node is a key, its corresponding value is a list of connected with an edge vertices/ nodes. The structure must be consistent, of course. Alternatively, you can use list of lists to represent the adjacency matrix for an undirected graph (an adjacency matrix is a square matrix used to represent a graph, where the value at position (i, j) in the matrix indicates whether there is an edge between vertex i and vertex j. Consistency in this case means that it is symmetric with zero diagonal).

Next, let's talk about trees. The simplest tree is a binary tree, a tree data structure in which each node has no more than two children: 2, 1, and for a leaf 0. An important kind is a binary search tree (BST) - "with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree"...shamelessly borrowed from Wikipedia article on [BST](https://en.wikipedia.org/wiki/Binary_search_tree). As a result, on average, the time complexity of search, insert, delete operations is O(log(n)) but in the worst case their time complexity is O(n). Although you can use specialised modules for graphs but for simple operations like sorting or searching it seems to be an overkill. By the way, you may need even more specialised BST structures like [red-black trees](https://en.wikipedia.org/wiki/Red–black_tree) or [AVL trees](https://en.wikipedia.org/wiki/AVL_tree).

Next, let's talk about [heaps](https://en.wikipedia.org/wiki/Heap_(data_structure)). They are helpful if you need to find and remove an element with the lowest/ largest score again and again while new elements are added to the data structure. In Python, min-heap is a kind of implemented in its standard library heapq which allow users to manipulate lists as priority queues or heaps. If you need a max-heap, just multiply all elements by -1. If all this about heaps is not very clear yet, just look in the code, it's really simple. What you need to remember that time complexity of popping the smallest element is constant, O(1), while insertion of a new element (with heappush method) is O(log(n)) time complexity. 




