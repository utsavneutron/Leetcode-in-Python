def rotate(self, matrix):
    #reverse
    def reverse(matrix):
        l = 0
        r = len(matrix) - 1

        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]

            l += 1
            r -= 1
    
    #transpose
    def transpose(matrix):
        for i in range(len(matrix)):
            for j in range(j):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    reverse(matrix)
    transpose(matrix)