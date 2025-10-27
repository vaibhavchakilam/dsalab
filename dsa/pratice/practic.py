class Solution:
    def mergeSort(self, nums):
        def sort(nums, low, high):
            if low < high:
                mid = (low + high) // 2
                sort(nums, low, mid)
                sort(nums, mid + 1, high)

                # Merge step
                temp = []
                left = low
                right = mid + 1

                while left <= mid and right <= high:
                    if nums[left] <= nums[right]:
                        temp.append(nums[left])
                        left += 1
                    else:
                        temp.append(nums[right])
                        right += 1

                while left <= mid:
                    temp.append(nums[left])
                    left += 1

                while right <= high:
                    temp.append(nums[right])
                    right += 1

                for i in range(len(temp)):
                    nums[low + i] = temp[i]

        sort(nums, 0, len(nums) - 1)  # Start recursive sort

# Example usage
nums = [7, 4, 1, 5, 3]
sol = Solution()
sol.mergeSort(nums)
print(nums)
