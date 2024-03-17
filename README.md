# Intermediate-Concepts-in-Python
## Intermediate Concepts and Best Practices in Python
Basic syntax, data types, common in-built data structures (strings, lists, tuples, sets, dictionaries), control flow methods (loops, conditionals, and functions), or importing modules (*.py files) probably don’t need any special demonstration. 

More  advanced concepts like object-oriented programming (including classes, instances and methods, data abstraction, inheritance, encapsulation, polymorphism, discussion of the OOP vs functional programming, etc), exception handling, file handling,  lambda functions (especially in list comprehension and for pandas series), generators, regular expressions, maps, collections, decorators will be demonstrated in this repo. It is important to test software as it is developed. The most basic level is formed by unit tests.
### Generators
In Python, a [generator](https://docs.python.org/3/tutorial/classes.html#generators) is a function which returns a generator iterator. It produces a series of values which can be retrieved one at a time with next() function. It's a call-by-need evaluation strategy sometimes called lazy evaluation. It saves memory. Run gen.py to see how it works.

A good illustration of generator's memory efficiency are Fibonacci numbers. Fibonacci sequence is used sometimes to illustrate recursion but it doesn't work well as a straightforward recursion (fib_new = fib_current + fub_previous) quickly runs out of memory. A generator only keeps track of the last two Fibonacci numbers generated. 

Another (practical) example is a countdown timer. Each second you call the generator to yield a new value. Generating permutations (or combinations) of elements, random sampling or file processing in batches saves memory as permutations, samples or batches are produced on the fly. This helps in Machine Learning for data preprocessing or cleaning, image resizing/ cropping in face recognition systems, log file analysis, etc. Generators can be used to implement asynchronous programming patterns, enabling concurrent execution (e.g. real-time data sreaming) of tasks without the complexity of traditional threading or multiprocessing.

###Lambda functions
Lambda functions are anonymous functions (=functions without a name). They are defined using the lambda keyword and can take any number of arguments but can only have one expression. Lambda functions are used in situations where you need a small function for a short period of time and don't want to define a full-fledged function using the def keyword. (Please see a collection of simple examples in lambda_demo.py).

It makes sense to use a lambda function with iterables (such as lists, strings, tuples, dictionaries) in order to produce another iterable, e.g. to filter a list. If you sort a list of tuples, strings or dictionaries based on some parameter, use this parameter as a key. Using such key also helps if you need an element with the largest or smallest value of the parameter, say a person who gets the largest salary in your organisation. Some people say that list comprehension with anonymous functions looks particularly "pythonic". It's a matter of taste but sometimes applying lambda functions too freely may produce unexpected results (I mean this example: squared_numbers = [lambda x: x**2 for x in numbers]). Also avoid complicated (e.g., nested conditionals) lambda functions as they make the code difficult to read. As lambda functions are simple by definition, you probably don't need to create test cases for them, just print out the result and compare with your expectations.

You can use a lambda function to modify another function and to assign it to a variable. For instance, first, define a multiplier, then by passing the correct multiplication factor (2 or 3) create a doubler or a tripler.


It's useful to know that lambda functions can help with writing a simple code for data transformation in a pandas series (= a column in a data frame).

You may find this link useful: ["How to Use Python Lambda Functions"](https://realpython.com/python-lambda/)



