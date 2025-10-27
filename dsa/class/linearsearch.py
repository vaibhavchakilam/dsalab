class Solution:
    def linearSearch(self, nums, target):
        n = len(nums)
        
        for i in range(n):
            if nums[i] == target:
                return i   # return index if found
        else:
            return -1     # if not found

# Example usage
sol = Solution()
nums = [10, 5, 12, 3, 1, 9]
print(sol.linearSearch(nums, 1))  # Output: -1 (not found)

