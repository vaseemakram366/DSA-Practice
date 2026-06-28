# Day-7: Topic-> Sorting Algorithms

# 1. write a program to impliment Selection sort on an array

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        # find minimum element in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # swap if needed
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


# Example usage
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)