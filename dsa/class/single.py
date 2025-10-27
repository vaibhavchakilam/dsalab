class Solution:
    def singleNumber(self, nums):
        n = len(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:   # ✅ check properly
                    count += 1
            if count == 1:               # ✅ only once means unique
                return nums[i]

sol = Solution()
nums = [1,1,3,3,4,4,6,6]
print(sol.singleNumber(nums))  # Output: 4
