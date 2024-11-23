# Output if a number is prime
# Number is prime if it is divisible by 1 and itself only
# 16 -> 1, 2, 4, 8, 16 -> NOT A PRIME NUMBER
# 17 -> 1, 17  -> PRIME NUMBER

number = 17

for i in range(2, number):
    if number % i == 0:
        print('Not a prime')
        break # Breaks always apply to the nearest loop, not the if statement

else:
    print('Is prime')