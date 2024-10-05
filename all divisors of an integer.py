"""Write a Python program to find all divisors of an integer or number using for loop. In this Python example, the for
 loop iterate from 1 to a given number and check whether each number is perfectly divisible by number.If True, print that number as the divisor."""


num = int(input("Please enter any integer to find divisors = "))

print("The Divisors of the Number = ")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)