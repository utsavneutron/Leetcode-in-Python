class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        ans = [[]]
        m = len(mat)
        n = len(mat[0])

        if m*n != r*c:
            return mat
        # print(m,n)

        for i in range(0, m):
            for j in range(0, n):
                temp = mat[i][j]
                # print(len(ans[-1]))
                if(len(ans[-1]) < c):
                    ans[-1].append(temp)
                else:
                    ans.append([temp])

        return ans
