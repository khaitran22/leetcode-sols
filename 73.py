def setZeroes(matrix):
    """
        Matrix (m, n)
        Time complexity: O(m x n)
        Space complexity: O(m + n)
    """
    cell_idxs = set()
    for r_idx, row in enumerate(matrix):
        for c_idx, col in enumerate(row):
            if col == 0:
                cell_idxs.add((r_idx, c_idx))
    
    for r_zero, _ in cell_idxs:
        for i in range(len(matrix[r_zero])):
            matrix[r_zero][i] = 0

    for _, c_zero in cell_idxs:
        for r in matrix:
            r[c_zero] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print(matrix == [[1,0,1],[0,0,0],[1,0,1]])