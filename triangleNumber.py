# https://leetcode.com/problems/valid-triangle-number/
# 611. Valid Triangle Number


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        answer = 0
        nums.sort()

        # loopin' time
        for i in range(n - 2, n):
            for j in range(n - 1, n):
                for k in range(n):
                    if nums[i] + nums[j] > nums[k]:
                        answer += 1

        return answer


solution = Solution()
nums = [2, 2, 3, 4]
result = solution.triangleNumber(nums)
print(result)
