# 2. Write a program to implement Bubble sort on an array

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        # last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # optimization: stop if already sorted
        if not swapped:
            break
    
    return arr


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)