# 2. LeetCode 867 - Transpose Matrix

class Solution:
    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        ans = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                ans[j][i] = matrix[i][j]

        return ans