class Solution:
    def insertionSort(self, nums):
        n = len(nums)
        for i in range(1, n):
            current_value = nums.pop(i)  # Remove element at index i
            insert_index = i
            for j in range(i - 1, -1, -1):
                if nums[j] > current_value:
                    insert_index = j
            nums.insert(insert_index, current_value)  # Insert at correct position
sol = Solution()
nums = [7, 4, 1, 5, 3]
sol.insertionSort(nums)
print(nums)