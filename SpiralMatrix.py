def spiral_matrix(matrix):
    if matrix is None: return
    m = len(matrix)
    if m == 0: return
    n = len(matrix[0])

    top = left = 0
    bottom = m-1
    right = n-1

    while top <= bottom and left <= right:

        for i in range(left, right+1):
            print matrix[top][i]
        top += 1

        print "-----"

        for i in range(top, bottom+1):
            print matrix[i][right]
        right -= 1

        print "-----"

        if top <= bottom:
            for i in range(right, left-1, -1):
                print matrix[bottom][i]
            bottom -= 1

        print "-----"

        if left <= right:
            for i in range(bottom, top-1, -1):
                print matrix[i][left]
            left += 1

        print "-----"


a = [ [1, 2, 3, 4, 5, 6],
      [7, 8, 9, 10, 11, 12],
      [13, 14, 15, 16, 17, 18] ]

spiral_matrix(a)
