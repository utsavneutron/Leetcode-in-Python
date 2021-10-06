# https://leetcode.com/problems/rotate-image/

# 90 degree = reverse and transpose
# 180 degree = reverse, transpose, reverse and transpose
#270 degree = transpose and reverse

def rotateImg(self, matrix):
    #reverse
    l = 0
    r = len(matrix) - 1

    while l < r:
        matrix[l], matrix[r] = matrix[r], matrix[l]
        l += 1
        r -= 1
    
    #transpose
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    #90 degree rotation
    # We want to rotate
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]
    # ->
    # [7, 4, 1],
    # [8, 5, 2],
    # [9, 6, 3]]

    # We can do this in two steps.
    # Reversing the matrix does this:
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]]
    # ->
    # [7, 8, 9],
    # [4, 5, 6],
    # [1, 2, 3]

    # Transposing means: rows become columns, columns become rows.

    # [7, 8, 9],
    # [4, 5, 6],
    # [1, 2, 3]
    # ->
    # [7, 4, 1],
    # [8, 5, 2],
    # [9, 6, 3]




    # 180 degree Rotation
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]
    # ->
    # [9, 8, 7],
    # [6, 5, 4],
    # [3, 2, 1]

    # Transposing means: rows become columns, columns become rows.

    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]
    # ->
    # [1, 4, 7],
    # [2, 5, 8],
    # [3, 6, 9]

    # Reverse:
    # [1, 4, 7],
    # [2, 5, 8],
    # [3, 6, 9]
    # ->
    # [3, 6, 9],
    # [2, 5, 8],
    # [1, 4, 7]

    # Transposing means: rows become columns, columns become rows.

    # [3, 6, 9],
    # [2, 5, 8],
    # [1, 4, 7]
    # ->
    # [3, 2, 1],
    # [6, 5, 4],
    # [9, 8, 7]

    # Reverse:
    # [3, 2, 1],
    # [6, 5, 4],
    # [9, 8, 7]
    # ->
    # [9, 8, 7],
    # [6, 5, 4],
    # [3, 2, 1]


    
    # 270 degree
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]
    # ->
    # [3, 6, 9],
    # [2, 5, 8],
    # [1, 4, 7]

    # Transposing means: rows become columns, columns become rows.

    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]
    # ->
    # [1, 4, 7],
    # [2, 5, 8],
    # [3, 6, 9]

    # Reverse:
    # [1, 4, 7],
    # [2, 5, 8],
    # [3, 6, 9]
    # ->
    # [3, 6, 9],
    # [2, 5, 8],
    # [1, 4, 7]
