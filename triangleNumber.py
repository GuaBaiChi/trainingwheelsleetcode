# https://leetcode.com/problems/valid-triangle-number/
# 611. Valid Triangle Number


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        nums.sort()
        for i in nums[-2:n]:
            for j in nums[-1:n]:
                for k in nums:
                    if nums[i] + nums[j] > nums[k]:
                        count += 1
        return count


solution = Solution()
nums = [2, 2, 3, 4]
result = solution.triangleNumber(nums)
print(result)


# class Solution:
#     def triangleNumber(self, nums: list[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         answer = 0

#         for k in range(2, n):
#             i, j = 0, k-1
#             while i < j:
#                 if nums[i] + nums[j] > nums[k]:
#                     answer += j - i
#                     j -= 1
#                 else:
#                     i += 1

#         return answer
