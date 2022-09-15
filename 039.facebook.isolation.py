# K is space that need to be left
# S is the list of seats already taken
# N is total number of seats
from typing import List
import math


def maxRemainingSeats(N: int, S, K: int, M) -> int:
    S.sort()
    maxs = 0
    start = int(max(S[0]-1, 0)/(K+1))
    end = int(max(N-S[-1], 0)/(K+1))
    maxs += start + end
    for i in range(1, M):
        bseats = S[i] - S[i-1] - 1
        nseat_gap = 2 * K + 1
        maxs += int(max(bseats-nseat_gap, 0)/(K+1))
        if bseats >= nseat_gap:
            maxs += 1
    return maxs


print(maxRemainingSeats(10, [2, 6], 1, 2))  # should be 3
print(maxRemainingSeats(15, [11, 6, 14], 2, 3))  # should be 1

# 1 2* 3 4^ 5 6* 7 8^ 9 10^
# 1 2 3^ 4 5 6* 7 8 9 10 11* 12 13 14* 15
