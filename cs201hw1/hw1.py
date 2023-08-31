# O(1) example [Constant Time]
def constant_time_example(array):
    return array[1]

array = [1, 2, 3, 4, 5]
result = constant_time_example(array)
print("Constant Time Example: Retrieving An Array Element")
print("We will print the second element of this array: [1, 2, 3, 4, 5]")
print(result)

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
target2 = 3
target3 = 9
index = binary_search(sorted_array, target)
index2 = binary_search(sorted_array, target2)
index3 = binary_search(sorted_array, target3)
print("Logarithmic Time Example: Binary Search")
print("We start with this array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
print("and will then find the index of 7, 3, and 9, in that order.")
print("Indices:")
print(index) 
print(index2)
print(index3)


# O(n) example [Linear Time]:
def linear_time_example(array):
    total_sum = 0
    for num in array:
        total_sum += num
    return total_sum

array = [1, 2, 3, 4, 5]
array2 = [2, 3, 4, 5]
array3 = [3, 4, 5, 7]
result = linear_time_example(array)
result2 = linear_time_example(array2)
result3 = linear_time_example(array3)
print("Linear Time Example: Adding All Elements In An Array")
print("Three Arrays We Begin With: [1, 2, 3, 4, 5], [2, 3, 4, 5], [3, 4, 5, 7]")
print(result)
print(result2)
print(result3)


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
array2 = [6, 4, 9, 1, 8, 1, 5, 4]
array3 = [5, 9, 10, 21, 2, 1, 7, 4]
sarray = merge_sort(array)
sarray2 = merge_sort(array2)
sarray3 = merge_sort(array3)
print("Quasilinear Time Example: Merge Sort")
print("Original Three Arrays: [5, 3, 8, 2, 7, 1, 6, 4], [6, 4, 9, 1, 8, 1, 5, 4], [5, 9, 10, 21, 2, 1, 7, 4]")
print("Sorted Arrays:")
print(sarray)
print(sarray2)
print(sarray3)



# O(n^2) example [Quadratic Time]:
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

array = [5, 3, 8, 2, 7, 1, 6, 4]
array2 = [6, 4, 9, 1, 8, 1, 5, 4]
array3 = [5, 9, 10, 21, 2, 1, 7, 4]
bubble_sort(array)
bubble_sort(array2)
bubble_sort(array3)
print("Quadratic Time Example: Bubble Sort")
print("Original Three Arrays: [5, 3, 8, 2, 7, 1, 6, 4], [6, 4, 9, 1, 8, 1, 5, 4], [5, 9, 10, 21, 2, 1, 7, 4]")
print("Sorted Arrays:")
print(array)
print(array2)
print(array3)


# O(n!) example [Factorial Time]
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
result2 = factorial(7)
result3 = factorial(9)
print("Factorial Time Example: Factorial Calculation")
print("Factorials will be calculated for 5, 7, and 9, in order.")
print(result)  
print(result2)
print(result3)