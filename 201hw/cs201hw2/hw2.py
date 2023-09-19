# homework 2 - cs 201


# Q2
def print_natural_numbers(n):
    if n > 0:
        print_natural_numbers(n - 1)
        print(n, end=' ')

# Example usage:
print("First 50 natural numbers:")
print_natural_numbers(50)
print("\n")


#Q3
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Example usage:
result = fibonacci(10)
print("Fibonacci Series (first 10 numbers):", result)
print("\n")


#Q4
def print_array(arr, index):
    if index < len(arr):
        print(arr[index], end=' ')
        print_array(arr, index + 1)

# Example usage:
my_array = [1, 2, 3, 4, 5]
print("Array elements:")
print_array(my_array, 0)
print("\n")


#Q5
def count_digits(number):
    if number == 0:
        return 0
    else:
        return 1 + count_digits(number // 10)

# Example usage:
num1 = 12345
num2 = 987654321
num3 = 0

print("Number of digits in", num1, "is", count_digits(num1))
print("Number of digits in", num2, "is", count_digits(num2))
print("Number of digits in", num3, "is", count_digits(num3))
print("\n")


#Q6
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

# Example usage:
num = int(input("Input any number to find the sum of digits: "))
result = sum_of_digits(num)
print(f"The Sum of digits of {num} = {result}")
print("\n")


#Q7
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example usage:
print("Finding greatest common denominator:")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")
print("\n")


#Q8
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
num = int(input("Enter a number to find its factorial: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")
print("\n")


#Q9
def is_prime(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)

# Example usage:
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
print("\n")


#Q10
def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])

# Example usage:
word = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
