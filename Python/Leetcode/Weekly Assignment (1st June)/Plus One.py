'''
Que : You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

'''

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
  
        if i < 0:  # Need to prepend a 1 for overflow
            return [1] + digits
        else:
            digits[i] += 1
        return digits
    
plus_one = Solution()
# Test Case 

l1 = [1,2,3]
print(plus_one.plusOne(l1))

l2 = [9]
print(plus_one.plusOne(l2))

