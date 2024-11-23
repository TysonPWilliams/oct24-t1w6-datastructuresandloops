# Function - Reusable collection of code that performs a particular task

# Defining a function. The parameter 'name', 'age' and 'country' is only scoped locally, it only exists within this function, it can't be called outside of the function.
def greet(name, age, country='Australia'):
    print(f'Hello {name}! You are {age} years old!')
    print(f'You live in {country}.')
    print(f'Goodbye {name}! Have a great day.')
    

# Calling the function. 
greet(age=29, name='Tyson')


greet('Mary', 21, 'NZ')