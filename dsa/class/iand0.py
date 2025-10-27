class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current = 0
        
        for num in nums:
            if num == 1:
                current += 1
            else:
                current = 0
            if current > max_count:
                max_count = current
        
        return max_count


sol = Solution()
nums = [1,0,1,1,1,1,1,0]
print(sol.findMaxConsecutiveOnes(nums))
