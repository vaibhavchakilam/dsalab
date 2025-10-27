def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        # Recursive calls in the same function
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)

        # Merging step (inside same function)
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(len(temp)):
            arr[low + i] = temp[i]


# Example usage
arr = [1, 3, 5, 2, 6, 8, 4, 2, 1, 10]
merge_sort(arr, 0, len(arr) - 1)
print(arr)
