def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # Write your code here
    tab = [None] * K
    ti = 0
    eat = 0
    for i in range(N):
        check = D[i]
        if check not in tab:
            eat += 1
            tab[ti] = check
            ti = (ti + 1) % K
    return eat


def getMaxEatDish(N, D, K):
    dish = {}
    eat = 0
    for i in range(N):
        if D[i] not in dish.keys() or eat - dish[D[i]] >= K:
            eat += 1
            dish[D[i]] = eat

    return eat
