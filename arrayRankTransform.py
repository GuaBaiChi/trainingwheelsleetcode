# https://leetcode.com/problems/rank-transform-of-an-array/
# 1331. Rank Transform of an Array


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        dmap = {}
        sortedarr = sorted(list(set(arr)))
        ranks = []

        for i in range(len(sortedarr)):
            dmap[sortedarr[i]] = i + 1
        for i in arr:
            ranks.append(dmap[i])
        return ranks


# driver code
solution = Solution()
arr = [40, 10, 20, 30]
print(solution.arrayRankTransform(arr))
