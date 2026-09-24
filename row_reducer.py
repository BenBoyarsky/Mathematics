import numpy as np

#Assume A has one solution  --> convenient pivots
def reduce(A):
    M = A.astype(float)
    M_next = M.copy()
    num_rows = M.shape[0]
    num_cols = M.shape[1]

    #reduce each column below pivot
    for j in range(num_cols - 1): 
        #get a nonzero num to pivot
        pivot = (j, j)
        if M_next[pivot] == 0:
            for i in range(j+1, num_rows):
                if not M_next[i, j] == 0:
                    rowA = M_next[j].copy()
                    rowB = M_next[i].copy()
                    M_next[j] = rowB
                    M_next[i] = rowA
                    break
        #normalize pivot
        M_next[j] /= M_next[pivot]

        #put zeros under pivot
        for i in range(j+1, num_rows):
            a = (-1) * (M_next[i, j] / M_next[pivot])
            M_next[i] += a * M_next[j]

        print(M_next, '\n')

    #reduce each column 
    #for j in range(num_cols-2:-1:-1):
        
 
    return M_next

A = np.array([

    [2,  1, -1,  0,  3,  10],

    [1, -2,  2,  1, -1,  -3],

    [3,  1,  1, -2,  2,  12],

    [1,  3, -1,  2,  1,   7],

    [2, -1,  3,  1,  2,   8]

])
print(reduce(A))