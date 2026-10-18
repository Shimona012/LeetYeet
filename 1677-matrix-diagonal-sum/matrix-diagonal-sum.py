class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        sum_mat = 0
        for i in range(n):
            sum_mat += mat[i][i]
            sum_mat += mat[i][n-1-i]
        if n % 2 != 0:
            sum_mat -= mat[n//2][n//2]
        return sum_mat
     