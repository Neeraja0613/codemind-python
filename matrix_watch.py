class Solution:
    def searchMatrix(self, mat, x):
        # code here
        for i in mat:
            for j in i:
                if j==x:
                    return True
        return False
