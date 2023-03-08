# https://leetcode.com/problems/complement-of-base-10-integer/
# 1009. Complement of Base 10 Integer


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        numberbin = bin(n)
        returnbinary = ""

        for i in numberbin[2:]:
            if i == "0":
                returnbinary += "1"
            else:
                returnbinary += "0"

        return int(returnbinary, 2)


# driver code
numbers = 523
solution = Solution()
result = solution.bitwiseComplement(numbers)
print(result)
