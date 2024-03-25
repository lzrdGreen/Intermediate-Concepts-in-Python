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
Python has several built-in data structures, the most important include: lists, tuples, sets and dictionaries. They are all iterables (objects that can be iterated over with the help of a for loop). Another important iterable is an object called strings, they are not usually considered as data structures but rather a data type (an immutable sequence of characters). Sometimes strings along with float, integer and boolean variables are called primitive data structures.

These four data structures are so important and widely used that they are built in the language itself and optimised. (I often see some people claiming that Python has 4 built-in data structures which is definitely not true - see below examples of frozenset, another built-in data structure. It makes sense to read read the official Python documentation regarding [Built-in Types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)). They come with their own methods. Still you may need more advanced data structures (to store and organise your data) - some of them can be imported from existing libraries, others are user-defined. The choice of data structure depends on the requirements of your problem: which operations needs to be the most efficient - searching? sorting? insertion/ deletion? Understanding the strengths and weaknesses of the data structure you use is crucial.

**Queues:** first-in-first-out (FIFO) data structures useful in modelling waiting lines (=queues) and breadth-first search.

**Stacks:** last-in-first-out (LIFO) data structures useful for recursive algorithms and undo operations - visualise LIFO as a stack of plates.

**Graphs:** collections of nodes (vertices) and edges (links) that represent some kind of relationship between the objects represented by nodes. Graphs can represent chemical structures, social networks, help find the shortest path in route planning, etc. Graphs are very well studied in the graph theory and computer science. Even if you can't have an exact solution, quite often you can have an approximate algorithm which produces a reasonably good result (the travelling salesperson problem, TSP, is NP-hard but you have some algorithms which normally give you a route that is slightly worse than the optimal route). Graphs can be directed or undirected.

**Trees:** hierarchical data structures with parent-child relationships, often used for efficient searching and sorting. In graph theory a tree is an undirected graph in which any two nodes are connected by exactly one edge, and there are no cycles. In computer science a tree is also a graph (a directed acyclic graph - DAG) which has a root (a node without any parent), nodes (with a parent and children) and leaves (nodes without children). It looks like a flipped over tree. Binary trees are extremely often used.

There is a number of list-like data structure: stacks/ queues, arrays, numpy arrays, linked lists, circular linked lists - to name a few.

The natural extension for tuples are namedtuples.

There are various dictionary-like structures: hash tables (in fact, a dictionary in Python is a kind of hash table under the hood), OrderedDict, etc

Some other data structures: heaps, priority queues, tries (= prefix trees), various probabilistic data structures (Bloom filters, Bayesian networks, Markov random fields). I am not going to discuss probabilistic data structures here as they are quite advanced.

All examples of implementation of data structures are presented in data_str.py.

I use deque objects (from the collections module) to implement both **stacks** and **queues** with most important methods for them: push and pop new elements, view the element to be popped next without removing it (peek), print out the stack/ queue, find out its length.

By the way, another useful object in the library collections is **Counter**. It is not a data structure, of course , but I included an example of how to use Counter anyway.

In Python dictionaries are unordered collections of key-value pairs. Keys are immutable (can't be changed, either add or delete) but the values are easy to assign a new value. You may need a dictionary-like structure which remembers the order in which its elements were added: **OrderedDict**, a dictionary subclass from the collections. It maintains the order of insertion, unlike regular/ built-in dictionaries which may reorder the elements for efficiency.

Named tuples are also included in the collections module. The idea is to make the data easy to recognise - I use a named tuple for a point in 2 dimensions.

Another example of using hash tables (for efficiency, of course) in disguise: sets in Python are implemented using hash tables under the hood. Hash tables are a common data structure for implementing sets because they provide efficient average-case time complexity for common set operations such as membership testing, insertion, and deletion.Sets are typically used for storing mutable collections of unique elements. They are useful for tasks like removing duplicates from a list, performing set operations like union, intersection, difference, and symmetric difference, and testing membership of elements. Frozensets: Frozensets are useful when you need an immutable collection of unique elements, such as when you want to use a set-like object as a key in a dictionary or as an element in another set. Frozensets are also hash tables under the hood, utilizing a similar mechanism for efficient storage and retrieval of elements. However, because frozensets are immutable, they do not need to support operations that modify their contents like sets do.  

Now you need to install these modules:matplotlib, networkx.I recommend using: conda install networkx matplotlib (if you installed your Python using Miniconda or Anaconda).

First I create a simple graph G1, just as a demonstration how to use networkx module. The next graph G2 is used to show Dijkstra's algorithm, which finds the shortest path between nodes. The module has a built-in method for Graph() objects for this operation. You may wish to take a look at an implementation of the [Dijkstra's algorithm in Python](https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html) from scratch. An interesting thing about Dijkstra's algorithm is that it is "greedy", i.e. it builds the path by always going to the nearest next node.

Next I show how to use a queue, the data sructure we discussed at the beginning, for search, to be specific, for breadth-first search (BFS). Please note that I represent a graph as a dictionary: each node is a key, its corresponding value is a list of connected with an edge vertices/ nodes. The structure must be consistent, of course. Alternatively, you can use list of lists to represent the adjacency matrix for an undirected graph (an adjacency matrix is a square matrix used to represent a graph, where the value at position (i, j) in the matrix indicates whether there is an edge between vertex i and vertex j. Consistency in this case means that it is symmetric with zero diagonal).

Next, let's talk about trees. The simplest tree is a binary tree, a tree data structure in which each node has no more than two children: 2, 1, and for a leaf 0. An important kind is a binary search tree (BST) - "with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree"...shamelessly borrowed from Wikipedia article on [BST](https://en.wikipedia.org/wiki/Binary_search_tree). As a result, on average, the time complexity of search, insert, delete operations is O(log(n)) but in the worst case their time complexity is O(n). Although you can use specialised modules for graphs but for simple operations like sorting or searching it seems to be an overkill. By the way, you may need even more specialised BST structures like [red-black trees](https://en.wikipedia.org/wiki/Red–black_tree) or [AVL trees](https://en.wikipedia.org/wiki/AVL_tree).

Next, let's talk about [heaps](https://en.wikipedia.org/wiki/Heap_(data_structure)). They are helpful if you need to find and remove an element with the lowest/ largest score again and again while new elements are added to the data structure. In Python, min-heap is a kind of implemented in its standard library heapq which allow users to manipulate lists as priority queues or heaps. If you need a max-heap, just multiply all elements by -1. If all this about heaps is not very clear yet, just look in the code, it's really simple. What you need to remember is that time complexity of popping the smallest element is constant, O(1), while insertion of a new element (with heappush method) has O(log(n)) time complexity. For queues and stacks the time complexity of push and pop operations is O(1), while search is O(n).

### Object-Oriented Programming (OOP) in Python
Are you ready to embark on a journey where coding becomes as playful as building with Legos? Picture this: you have a desire to create, to construct not just one, but countless imaginative creations, each with its own unique flair. What if I told you there's a way to do just that in the world of programming? Welcome to the captivating realm of Object-Oriented Programming (OOP) in Python, where concepts like classes and inheritance are not just abstract notions, but the building blocks of limitless digital innovation. Let's dive in and unravel the magic of Python's OOP, where coding becomes akin to crafting your own universe, one class at a time.

**Classes and Objects:**
Imagine you have a magical Lego instruction booklet that shows you how to build a spaceship. This booklet is like a class in Python. It tells you exactly what pieces you need and how to put them together. Now, when you actually use this booklet to build your spaceship, that's like creating an object. Each object is a unique spaceship that follows the instructions from the class.

**Instances:**
When you build your spaceship using the instruction booklet, you're making an instance of that spaceship. It's like making a real version of what the instructions show. So, if you want to build ten spaceships, you make ten instances, each following the same instructions but ending up as separate spaceships.

**Methods and Attributes:**
Now, let's talk about what your spaceship can do and what it's made of. Attributes are like the special features of your spaceship, such as its color, size, and the number of engines it has. Methods, on the other hand, are the cool things your spaceship can do, like flying, making laser sounds, or even transforming into a robot! Just like how your spaceship needs specific Lego pieces to have certain features, attributes are the characteristics your object possesses, while methods are the actions it can perform.

**Basic Inheritance Example:**
Imagine you've built a marvelous Lego vehicle, a sleek race car with wheels and a steering wheel. Now, your imagination sparks a desire to construct a monstrous truck. But before you start from scratch, think about this: both the race car and the monster truck share common components, like wheels and a steering wheel. Rather than reinventing the wheel (pun intended), you can capitalize on what you've already crafted for the race car and expand upon it to fashion the monster truck.

In Python, this concept aligns with inheritance. Picture the Vehicle class as the parent, serving as the blueprint for all types of vehicles. Within this class lie the fundamental features shared by vehicles, like wheels and steering. Now, envision the race car and the monster truck as child classes derived from the Vehicle class. By inheriting from the Vehicle parent class, both vehicles inherit its basic attributes, such as wheels and steering.

However, inheritance doesn't stop there. With the monster truck class, you have the flexibility to introduce additional attributes and methods specific to this mighty vehicle, such as oversized tires and a thunderous roar. This process allows you to build upon the foundation established by the Vehicle class, enhancing each creation with unique characteristics while minimizing redundancy: with inheritance, you're not starting from square one every time you build something new. Instead, you're building upon the foundation you've already laid, infusing each creation with its own distinctiveness and excitement, much like adding extra features to your Lego masterpieces to make them even cooler and more thrilling!

In essence, inheritance empowers you to extend and customize existing code, much like adding new features to your Lego creations, transforming them into something even more extraordinary.
(A note of caution: the above part of section on OOP in Python was actually written by ChatGPT 3.5 based on examples I asked to produce Google's Gemini Nano, the simplest, with minor editing A bit too wordy to my taste, but tastes differ...

By the way, Google seems to have silently made a break-through noone noticed: they trained a small LLM, I mean it: SMALL large language model. Their Gemini Nano nicely works on my Pixel 6 off-line! Google claimed that the smallest Gemini Nano has 1.8 billion parameters only - to fit in your device memory. For comparison GPT 3.5 has 175 billion parameters, GPT 4 - nobody knows for sure but Google competitors estimate it as 1 trillion. I am sure Google used neural network distillation for its Gemini Nano training, very likely pruning and quantization. But what else?)

**A simple examplle**
Now I must write some idiotic Python code with all those car-like classes producing actions like car.signal() method and "make" attribute. Instead, I am going to use class PriorityQueue as a simple example - please see oop_demo.py.

**Class** PriorityQueue: In Python, a class is like a blueprint for creating objects. It defines the properties and behaviors of objects.
**Object/Instance** pq = PriorityQueue(): An object is a specific instance of a class. It represents a concrete occurrence of the class and has its own unique state and behaviour.

**Attributes:**
In the PriorityQueue class, _queue and _index are attributes (internal data). _queue is a list that holds items along with their priorities, and _index is used to ensure that items with the same priority are ordered based on their insertion order.

**Methods:**
__init__: This method is the constructor of the class. It initializes the _queue as an empty list and _index as 0.
push: This method adds an item to the priority queue along with its priority. It uses the heappush function from the heapq module to maintain the heap invariant.
pop: This method removes and returns the item with the highest priority from the priority queue. It uses the heappop function from the heapq module to maintain the heap invariant.
__len__: This method returns the length of the queue.
Please note: The methods __init__ and __len__ in Python classes are examples of special methods, also known as double underscore methods. These special methods have reserved names that Python recognizes and calls implicitly in specific situations: when you define __init__ and __len__ methods in a class, Python knows how to handle object initialization and length computation automatically, making your code more intuitive and consistent with Python's conventions. Other common examples include: __str__, __getitem__, __setitem__, __iter__, __next__, __eq__ and so on.

We also have one more class in oop_demo.py: TestPriorityQueue.
**Class Definition:** The TestPriorityQueue class is defined as a subclass of unittest.TestCase. Inheritance is a fundamental concept in OOP, where a class (subclass) can inherit attributes and methods from another class (superclass).
**Purpose of the Class:** The purpose of the TestPriorityQueue class is to encapsulate test cases that verify the functionality of the PriorityQueue class. This encapsulation aligns with the principle of encapsulation in OOP, where related data and methods are grouped together within a class.
**Methods:** The class contains test methods such as test_push_pop and test_empty_queue. These methods represent behaviors or actions that validate specific aspects of the PriorityQueue class.
**Inheritance:** The TestPriorityQueue class inherits from unittest.TestCase, which is a superclass provided by the unittest module in Python. By inheriting from unittest.TestCase, TestPriorityQueue gains access to assertion methods (e.g., assertEqual, assertRaises) and the testing infrastructure provided by the unittest framework. This inheritance relationship highlights the concept of code reuse in OOP, where subclasses can leverage functionalities defined in their superclasses.