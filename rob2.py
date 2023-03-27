# https://leetcode.com/problems/house-robber-ii/
# 213. House Robber II
# renamed rob.py to rob2.py


class Solution:
    def best(self, nums: list[int]) -> int:
        previous_best = 0
        current_best = 0
        for num in nums:
            if previous_best + num > current_best:
                tmp = current_best
                current_best = previous_best + num
                previous_best = tmp
            else:
                previous_best = current_best
        return current_best

    def rob(self, nums: list[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        path_a = nums[1:]
        path_b = nums[: length - 1]
        return max(self.best(path_a), self.best(path_b))


# driver code
solution = Solution()
nums = [2, 3, 2, 4, 6]
result = solution.rob(nums)
print(result)
