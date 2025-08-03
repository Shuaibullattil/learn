def pre(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    prefix=[]

    for i in range(0,rows+1):
        row = [0]*(cols+1)
        prefix.append(row)
    
    # print(prefix)
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            prefix[i][j] = (matrix[i-1][j-1]+prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1])
    return prefix

def findsum(matrix,queries):
    prefixsum = pre(matrix)

    result = []
    for q in queries:
        topRow = q[0]+1
        LeftCol = q[1]+1
        bottomRow = q[2]+1
        rightCol = q[3]+1
        result.append(prefixsum[bottomRow][rightCol]
                      -prefixsum[topRow-1][rightCol]
                      -prefixsum[bottomRow][LeftCol-1]
                      +prefixsum[topRow-1][LeftCol-1])
    print(result)
mat = [[1, 2, 3],
        [1, 1, 0],
        [4, 2, 2]]
queries = [
        [0, 0, 1, 1],
        [1, 0, 2, 2]
    ]
findsum(mat,queries)



