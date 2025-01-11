def decreasing_insertion_sort(ar):
    """Sorting the given array in decreasing order using insertion sort."""

    for i in range(1, len(ar)):
        key = ar[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and key > ar[j]:
            ar[j + 1] = ar[j]
            j -= 1

        ar[j + 1] = key

# Sample Test:
ar = [27,60,16,7,10,89,1000,75,41,-1500,0,-90]
decreasing_insertion_sort(ar)
print("Decreasing Order of Sorted Array:", ar)