from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        memo = {}

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix) -1, -1, -1):
                left, mid, right = float("inf"), float("inf"), float("inf")
                if i + 1 <= len(matrix) - 1:
                    mid = memo[(i + 1, j)]
                    if j - 1 >= 0:
                        left = memo[(i + 1, j - 1)]
                    if j + 1 <= len(matrix) - 1:
                        right = memo[(i + 1, j + 1)]
                value = matrix[i][j]
                if min(left, mid, right) == float('inf'):
                    memo[(i, j)] = value
                else:
                    memo[(i, j)] = value + min(left, mid, right)

        res = float('inf')

        for key in memo:
            row, col = key
            if row == 0:
                res = min(memo[key], res)

        return res
