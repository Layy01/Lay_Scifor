'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
        return nums

# Test Case

move_zero = Solution()
nums1 = [0,1,0,3,12]
print(move_zero.moveZeroes(nums1))

nums2 = [0]
print(move_zero.moveZeroes(nums2))