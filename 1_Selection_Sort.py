def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Taking user input for the array
arr = input("Enter the elements of the array separated by space: ").split()
arr = [int(num) for num in arr]

# Sorting the array using selection sort
selection_sort(arr)

# Printing the sorted array
print("Sorted array is:", arr)
