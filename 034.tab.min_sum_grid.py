# Find the min sum path through a 2 dimensional array m x n starting at the [0][0] and ending at [m-1][n-1]. 
# Constrainted to only traverse the path by either going up or down.
import math

def minsumgrid(a):
    m = len(a)
    n = len(a[0])
    tab = [[math.inf for j in range(n)] for i in range(m)]
    tab[0][0] = a[0][0]
    for i in range(m):
        for j in range(n):
            if i == 0 and j ==0:
                continue
            if j > 0:
                right = tab[i][j-1]
            else:
                right = math.inf
            if i > 0:
                top = tab[i-1][j]
            else:
                top = math.inf
            tab[i][j] = min(right + a[i][j],top + a[i][j])
            #print(f"a[{i}][{j}] = {a[i][j]}, tab[{i}][{j}] = {tab[i][j]}")
    return tab[m-1][n-1]

print(minsumgrid([[1,3,1],[1,5,1],[4,2,1]]))