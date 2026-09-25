import numpy as np

#Assume A has one solution  --> convenient pivots
def reduce(A):
    M = A.astype(float)
    num_rows = M.shape[0]
    num_cols = M.shape[1]

    #reduce each column below pivot
    i = 0
    j = 0
    pivots = []
    while i < num_rows and j < num_cols: 
        #get a nonzero num to pivot if one exists
        pivot_exists = False
        if M[i, j] == 0:
            for k in range(i+1, num_rows):
                if (not M[k, j] == 0):
                    rowA = M[i].copy()
                    rowB = M[k].copy()
                    M[i] = rowB
                    M[k] = rowA
                    pivot_exists = True
                    break
        else:
            pivot_exists = True
        if not pivot_exists:
            j +=1
        else:
            pivots.append((i, j))
            #normalize pivot
            M[i] /= M[i, j]

            #reduce below pivot
            for k in range(i+1, num_rows):
                a = -1 * M[k, j]
                M[k] += a * M[i]
            i += 1
            j += 1
    del j
    del i

    #reduce above pivots
    for pivot in reversed(pivots):
        row, col = pivot
        for i in range(row-1, -1, -1):
            a = -1 * M[i, col]
            M[i] += a * M[row]
    
    return M

#assumes RR augmented matrix
def rank(A):
    M = A.copy()
    rows = M.shape[0]
    cols = M.shape[1]
    pivots = 0
    i = 0
    j = 0
    while i < rows and j < cols:
        if M[i, j] == 1:
            pivots += 1
            i += 1
            j += 1
        else:
            j += 1

    return pivots
            

A1 = np.array([

    [1, 2],

    [2, 4],

    [3, 6],

    [1, 3]

])
print(reduce(A1))

A = np.array([

    [1, 0, 3, 0],

    [0, 1, 2, 0],

    [0, 0, 0, 1]

])

#print(rank(A))



#still need to move 0 rows to lower area.