# List - (Array) - ordered collection of values - mutable (we can change the values that are contained within) - zero indexed
numbers = [13, 2, 23, 53]
print(numbers)
print(numbers[2])

# Changing a number in a list
numbers[2] = 17
print(numbers)

# How to add a single value into our list
numbers.append(42)
print(numbers)

# How to insert a value at a specific position in the list
numbers.insert(3, 99)
print(numbers)

# We can pop the last value off the list and then store it in a variable
popped_value = numbers.pop()
print(numbers)
print(popped_value)

numbers.pop(2)
print(numbers)

# Finds and removes the value 13 from the list. IF THERE ARE TWO OCCURENCES OF THE NUMBER 13, IT WILL REMOVE THE FIRST OCCURANCE ONLY
numbers.remove(13)
print(numbers)

numbers.append(13)
numbers.insert(0, 13)

# There are two different ways to pass paramaters, either keywork parameters like the below, or positional parameters like this: numbers.insert(3, 99)
numbers.sort(reverse=True)
print(numbers)

# Counting how many occurences of a value there are
print(numbers.count(13))






# Tuple - Ordered collection of values - zero indexed - immutable
names = ("John", "Jane", "Mike", "Mary")
print(names) 
print(type(names))

print(names[1])

# Prints what index the first occurence of Mike is at.
print(names.index('Mike'))
print(len('Hello'))