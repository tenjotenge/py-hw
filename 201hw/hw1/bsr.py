def binary_search_recursive(arr, target, low, high):
    # Base case: If the search interval is empty, the target is not in the array.
    if low > high:
        return -1  # Target not found

    # Calculate the middle index of the current search interval.
    mid = (low + high) // 2

    # If the middle element is equal to the target, return its index.
    if arr[mid] == target:
        return mid

    # If the target is smaller than the middle element, search in the left subarray.
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)

    # If the target is larger than the middle element, search in the right subarray.
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search_recursive(sorted_array, target, 0, len(sorted_array) - 1)

if result != -1:
    print(f"Element {target} is present at index {result}.")
else:
    print(f"Element {target} is not present in the array.")
