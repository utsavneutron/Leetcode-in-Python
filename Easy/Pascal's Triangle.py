class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return [[]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        pas = [[1], [1, 1]]

        for i in range(3, numRows+1):
            temp = [1]
            for j in range(1, i-1):
                temp.append(pas[-1][j-1] + pas[-1][j])

            temp.append(1)
            pas.append(temp)

        return pas
