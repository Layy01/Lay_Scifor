'''
Que : A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

'''

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()

        common_diff = arr[1] - arr[0]

        for i in range(1, len(arr) -1 ):
            if arr[i+1] - arr[i] != common_diff:
                return False
        return True
    
ap = Solution()

# Test Case 

arr1 = [1,3,5]
print(ap.canMakeArithmeticProgression(arr1))

arr2 = [1,3,5,7,8]
print(ap.canMakeArithmeticProgression(arr2))
