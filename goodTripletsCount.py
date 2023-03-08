# https://leetcode.com/problems/count-good-triplets/
# 1534. Count Good Triplets


class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        goodTripletsCount = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if (
                        abs(arr[i] - arr[j]) <= a
                        and abs(arr[j] - arr[k]) <= b
                        and abs(arr[i] - arr[k]) <= c
                    ):
                        goodTripletsCount += 1
        return goodTripletsCount


# driver code
solution = Solution()
arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3

print(solution.countGoodTriplets(arr, a, b, c))
