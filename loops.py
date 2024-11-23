# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# while loop
number = 1
while number <= 5:
    print(number)
    number += 1   # increment



# For loop
names = ['John', 'Jane', 'Mike', 'Mary']

# Creates a new list of tuples that attaches the index and element together.
# We're strapping the enumerate funttion to the for loop to create a tuple
for index, name in enumerate(names):
    print(f'{index+1}, {name}')


# List all numbers between 10 and 100 and state whether they are odd or even
for num in range(10, 101):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

print(f'{num} is {'even' if num % 2 == 0 else 'odd'}')

# for else

for i in range(10):
    print(i)
    if i == 6:
        break
else:
    print('loop finished')