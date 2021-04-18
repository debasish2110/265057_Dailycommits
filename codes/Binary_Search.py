
# Binary search using recursion.

def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1


arr = [2, 3, 4, 10, 40]
search_ele = 10

result = binary_search(arr, 0, len(arr) - 1, search_ele)

if result != -1:
    print("Element is present at index no: ",(result))
else:
    print("Element is not present in theK array")