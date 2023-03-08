# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# 1281. Subtract the Product and Sum of Digits of an Integer


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numbers = str(n)
        product = 1
        sum = 0

        for i in numbers:
            product *= int(i)
            sum += int(i)

        return product - sum


# driver code
solution = Solution()
n = 234
print(solution.subtractProductAndSum(n))
