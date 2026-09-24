import numpy as np

def reduce(A):
    M = A.astype(float)
    M_next = M.copy()
    num_rows = M.shape[0]
    num_cols = M.shape[1]

    #get a number to M11
    if M[0, 0] == 0:
        for i in range(1, num_rows):
            if not M[i, 0] == 0:
                row1 = M[0]
                row2 = M[i]
                M_next[0] = row2
                M_next[i] = row1
                break

    #subtract a * r1 from each row to make each row have 0 for the first position
    for i in range(1, num_rows):
        a = (-1) * (M_next[i, 0] / M_next[0, 0])
        M_next[i] += a * M_next[0]
 
    return M_next

A = np.array([[0, 3, -1, 4],
             [1, 2, 3, 3],
             [5, 0, 2, 0]])
print(reduce(A))