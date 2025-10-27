class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n - 1):
            min_val = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_val]:
                    min_val = j
            # Swapping using temp (your style)
            temp = nums[min_val]
            nums[min_val] = nums[i]
            nums[i] = temp
        return nums  # Don't forget to return the sorted list

sol = Solution()
nums = [1, 3, 5, 3, 7, 8, 44]
print(sol.selectionSort(nums))
