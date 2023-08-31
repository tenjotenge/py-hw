# O(1) example [Constant Time]
def constant_time_example(array):
    return array[0]

array = [1, 2, 3, 4, 5]
result = constant_time_example(array)
print(result)  # Output: 1

# O(log(n)) example [Logarithmic Time]:
def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
index = binary_search(sorted_array, target)
print(index)  # Output: 6 (index of 7 in the array)


# O(n) example [Linear Time]:
def linear_time_example(array):
    total_sum = 0
    for num in array:
        total_sum += num
    return total_sum

array = [1, 2, 3, 4, 5]
result = linear_time_example(array)
print(result)  # Output: 15 (sum of all elements)


# O(n log(n)) example [Quasilinear Time]
def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

array = [5, 3, 8, 2, 7, 1, 6, 4]
sorted_array = merge_sort(array)
print(sorted_array)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


# O(n^2) example [Quadratic Time]:
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

array = [5, 3, 8, 2, 7, 1, 6, 4]
bubble_sort(array)
print(array)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


# O(n!) example [Factorial Time]
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120 (5!)
