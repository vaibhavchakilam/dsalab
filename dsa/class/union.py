class Solution:
    def unionArray(self, nums1, nums2):
        z = nums1+nums2
        n = len(z)

        # bubble sort
        for i in range(n-1):
            for j in range(n-i-1):
                if z[j] > z[j+1]:
                    # proper swap
                    z[j], z[j+1] = z[j+1], z[j]

        # remove duplicates
        k = 0
        while k < len(z)-1:
            if z[k] == z[k+1]:
                del z[k]          # delete duplicate
            else:
                k += 1

        return z
sol = Solution()
nums1 =[1,2,3,4,5]
nums2 = [1,1,4,5,7]
print(sol.unionArray(nums1,nums2))