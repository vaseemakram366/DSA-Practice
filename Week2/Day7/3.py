# 3. Write a program to implement insertion sort on an array

def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # shift elements of sorted part that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # place key at correct position
        arr[j + 1] = key
    
    return arr


# Example usage
arr = [12, 11, 13, 5, 6]
print("Original array:", arr)

sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)