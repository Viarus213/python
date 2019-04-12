def heapify(arr, arrayLength, i):
    largest = i # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    print ("i =", i, " largest =", largest, " left =", left, " right =", right)

    # See if left child of root exists and is
    # greater than root
    if left < arrayLength and arr[i] < arr[left]:
        largest = left
        print ("largest = left")

    # See if right child of root exists and is
    # greater than root
    if right < arrayLength and arr[largest] < arr[right]:
        largest = right
        print ("largest = right")

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap

        # Heapify the root.
        heapify(arr, arrayLength, largest)

# The main function to sort an array of given size
def heapSort(arr):
    arrayLength = len(arr)

    # Build a maxheap.
    for i in range(arrayLength, -1, -1):
        heapify(arr, arrayLength, i)

    # One by one extract elements
    for i in range(arrayLength - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

# Driver code to test above
arr = [ 3, 12, 11, 13, 5, 6, 7, 1]
#arr = [1, 2, 3, 1, 1, 2, 3, 1]
heapSort(arr)

print ("Sorted array is")
print (arr)
