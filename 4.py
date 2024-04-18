class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 == 0:
            index1 = (len(nums)//2)-1
            index2 = ((len(nums)//2)+1)-1
            print(nums[index1] + nums[index2])
            median = (nums[index1] + nums[index2])/2
            return median
        else:
            index = len(nums)//2
            median = nums[index]
            return median

s1 = Solution()
print(s1.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))