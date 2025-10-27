class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        
        for r in range(n+1):
            if r  not in   nums:
                return r
                
sol =  Solution()
nums = [0,1,2,3,4]
print(sol.missingNumber(nums))       