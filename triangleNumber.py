# https://leetcode.com/problems/valid-triangle-number/
# 611. Valid Triangle Number
# https://www.youtube.com/watch?v=3Jo1NdD8xX4

# i <= j < k
# i + j > k

# [2, 3, 4, 4]
# [i, j, k, #]


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        answer = 0

        for k in range(2, n):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    answer += j - i
                    j -= 1
                else:
                    i += 1

        return answer


solution = Solution()
nums = [2, 2, 3, 4]
result = solution.triangleNumber(nums)
print(result)
