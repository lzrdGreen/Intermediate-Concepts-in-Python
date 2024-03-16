# Intermediate-Concepts-in-Python
## Intermediate Concepts and Best Practices in Python
Basic syntax, data types, common in-built data structures (strings, lists, tuples, sets, dictionaries), control flow methods (loops, conditionals, and functions), or importing modules (*.py files) probably don’t need any special demonstration. 

More  advanced concepts like object-oriented programming (including classes, instances and methods, data abstraction, inheritance, encapsulation, polymorphism, discussion of the OOP vs functional programming, etc), exception handling, file handling,  lambda functions (especially in list comprehension and for pandas series), generators, regular expressions, maps, collections, decorators will be demonstrated in this repo. It is important to test software as it is developed. The most basic level is formed by unit tests.
### Generators
In Python, a [generator](https://docs.python.org/3/tutorial/classes.html#generators) is a function which returns a generator iterator. It produces a series of values which can be retrieved one at a time with next() function. It's a call-by-need evaluation strategy sometimes called lazy evaluation. It saves memory. Run gen.py to see how it works.

A good illustration of generator's memory efficiency are Fibonacci numbers. Fibonacci sequence is used sometimes to illustrate recursion but it doesn't work well as a straightforward recursion (fib_new = fib_current + fub_previous) quickly runs out of memory. A generator only keeps track of the last two Fibonacci numbers generated. 

Another (practical) example is a countdown timer. Each second you call the generator to yield a new value. Generating permutations (or combinations) of elements, random sampling or file processing in batches saves memory as permutations, samples or batches are produced on the fly. This helps in Machine Learning for data preprocessing or cleaning, image resizing/ cropping in face recognition systems, log file analysis, etc. Generators can be used to implement asynchronous programming patterns, enabling concurrent execution (e.g. real-time data sreaming) of tasks without the complexity of traditional threading or multiprocessing.
