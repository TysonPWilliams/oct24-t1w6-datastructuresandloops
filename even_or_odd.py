# Function to determine if a number is even or odd

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(23))
result = even_or_odd(3)
even_or_odd(58)
print(f'3 is {result}')