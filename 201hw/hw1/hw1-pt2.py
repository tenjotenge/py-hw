def constant_summation(numbers):
    n = len(numbers)
    total_sum = (n * (n + 1)) // 2
    return total_sum

numbers = [1, 2, 3, 4, 5]
result = constant_summation(numbers)
print("Adding numbers from 1 to 5.")
print("Constant Time: ")
print(result)  # Output: 15 (1 + 2 + 3 + 4 + 5)

def linear_summation(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum

numbers = [1, 2, 3, 4, 5]
result = linear_summation(numbers)
print("Linear Time: ")  # Output: 15 (1 + 2 + 3 + 4 + 5)
print(result)