# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = digits[-1]
        if last == 9:
            if len(digits) == 1:
                return [1,0]
            return self.plusOne(digits[:-1]) + [0]
        digits[-1] += 1
        return digits