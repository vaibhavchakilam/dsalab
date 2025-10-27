class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        k=1  
        for i in range(0,n-1):
            if nums[i]!=nums[i+1]:
                nums[k] = nums[i] 
                k+=1
                
        return k        
sol = Solution()
nums = [0,0,1,1,2,3,4,5,5,6,6]    
print(sol.removeDuplicates(nums))