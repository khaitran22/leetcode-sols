# %%
# def celebrity(mat):
#     """
#         Brute-force approach
#     """
#     potential_celeb = set()
#     for idx_r, row in enumerate(mat):
#         curr_celeb = True
#         for idx_c, c in enumerate(row):
#             if c == 1 and idx_c != idx_r:
#                 curr_celeb = False
#                 break
#         if curr_celeb:
#             potential_celeb.add(idx_r)
#     actual_celeb = -1
#     for celeb in potential_celeb:
#         is_actual_celeb = True
#         for idx_r, row in enumerate(mat):
#             if row[celeb] == 0:
#                 is_actual_celeb = False
#         if is_actual_celeb:
#             actual_celeb = celeb
#     return actual_celeb

def celebrity(mat):
    """
        Two pointer approach:
        Space: O(1)
        Time: O(n)
    """
    i = 0
    j = len(mat) - 1
    while i < j:
        if mat[i][j] == 1:
            i += 1
        else:
            j -= 1
    
    for idx, c in enumerate(mat[i]):
        if c == 1 and idx != i:
            return -1
        
    for row in mat:
        if row[i] == 0:
            return -1
    
    return i

mat = [[1, 1, 1],
        [0, 1, 0],
        [1, 0, 1]]
# mat = [[1]]
# mat = [[1, 1], 
#                 [1, 1]]
print(celebrity(mat))
# %%
