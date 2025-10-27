class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    # Swap using temp
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
        return nums

sol = Solution()
nums = []

