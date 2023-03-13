# https://leetcode.com/problems/house-robber-ii/
# 213. House Robber II
# renamed rob.py to rob2.py


class Solution:
    def rob(self, nums: list[int]) -> int:
        odd = 0
        even = 0
        numslength = len(nums)

        if numslength % 2 == 0:
            for i in range(1, len(nums[1:]), 2):
                element = nums[i]
                odd += element
        else:
            for i in range((1, len(nums), 2)):
                element = nums[i]
                even += element

        if odd > even:
            return odd
        else:
            return even


# for i in range(1,11,2):

# driver code
solution = Solution()
nums = [2, 3, 2, 4, 6]
result = solution.rob(nums)
print(result)


# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         countera1 = 0
#         countera2 = 0

#         for num in nums[:-1]:
#             temp = countera1
#             countera1 = max(countera2 + num, countera1)
#             countera2 = temp

#         counterb1 = 0
#         counterb2 = 0
#         for num in nums[1:]:
#             temp = counterb1
#             counterb1 = max(counterb2 + num, counterb1)
#             counterb2 = temp

#         return max(countera1, counterb1)
