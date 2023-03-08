# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/
# 2231. Largest Number After Digit Swaps by Parity


class Solution:
    def largestInteger(self, num: int) -> int:
        number = str(num)
        odd = []
        even = []

        for i in number:
            if int(i) % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        sortedeven = sorted(even)
        sortedodd = sorted(odd)

        output = ""
        for nums in number:
            if int(nums) % 2 == 0:
                output += sortedeven.pop()
            else:
                output += sortedodd.pop()

        return int(output)


num = 12345666
solution = Solution()
result = solution.largestInteger(num)
print(num)
print(result)


# other ways to convert an int to a str
# #1
# num_str = ""
# for n in reversenums:
#    num_str += n

# #2
# num_str = ""
# for i in range(len(nums)):
#    num_str += nums.pop()

# # 3
# num_str = ""
# for num in nums:
#     num_str = num + num_str

# # 4
# num_str = ''.join(reverse_nums)
