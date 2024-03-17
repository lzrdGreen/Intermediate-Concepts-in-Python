# create a list of numbers from 0 to 9 using list comprehension
numbers = [x for x in range(10)]
#print (numbers)

# Example of using map() with lambda function
squared_numbers = list(map(lambda x: x**2, numbers))
#print(squared_numbers)

# Example of using filter() with lambda function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#print(even_numbers)

# A silly example of using sorted() with lambda function
numbers = [5, 2, 3, 1, 4]
desc_sorted_numbers = sorted(numbers, key=lambda x: -x) 
#use built-in function for lists instead
sorted_numbers_desc = sorted(numbers, reverse=True)
#print(desc_sorted_numbers, sorted_numbers_desc)

# Sorting a list of strings based on the length of each string
words = ['banana', 'apple', 'orange', 'strawberry', 'kiwi']
sorted_words = sorted(words, key=lambda x: len(x))
#print(sorted_words)

# Sorting a list of dictionaries based on a specific key
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_people = sorted(people, key=lambda x: x['age'])
#print(sorted_people)

# Sorting a list of tuples based on the second element using a lambda function
points = [(1, 5), (3, 2), (2, 8), (5, 4)]
sorted_points = sorted(points, key=lambda x: x[1])
#print(sorted_points)



# Example of list comprehension using lambda function for transformation
numbers = [1, 2, 3, 4, 5]
# you get nonsense if you try this:
squared_numbers = [lambda x: x**2 for x in numbers]
print(squared_numbers)
#instead use lambda function with map:
print(list(map(lambda x: pow(x, 2), numbers)))

# Creating a function that returns a lambda function
def multiplier(n):
    return lambda x: x * n

doubler = multiplier(2)
tripler = multiplier(3)
#print(doubler(5), tripler(5))



