class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        j = 0  # pointer for placing non-zero elements
        
        # Move all non-zero elements to the front
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
      
class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        j = 0  # pointer for placing non-zero elements
        
        # Move all non-zero elements to the front
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        # Fill the rest with zeroes
        for i in range(j, n):
            nums[i] = 0
        
        return nums

# Example usage
sol = Solution()
nums = [1, 0, 2, 0, 3, 4, 0, 5]
print(sol.moveZeroes(nums))  # Output: [1, 2, 3, 4, 5, 0, 0, 0]

# Example usage
sol = Solution()
nums = [1, 0, 2, 0, 3, 4, 0, 5]
print(sol.moveZeroes(nums))  # Output: [1, 2, 3, 4, 5, 0, 0, 0]
