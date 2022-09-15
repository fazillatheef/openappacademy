def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    # Write your code here
    ct_def = 0
    if N == 1 or N == 0:
        return 0
    curr_disc = R[N-1]
    for i in range(N-2, -1, -1):  # (eg: N=8 , 7, 6 , ... , 0)

        if R[i] >= curr_disc:
            curr_disc = curr_disc - 1
            if curr_disc < 1:
                return -1
            ct_def += 1
        else:
            curr_disc = R[i]

    return ct_def
