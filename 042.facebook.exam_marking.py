def getMinProblemCount(N: int, S: List[int]) -> int:
    odd = False
    for num in S:
        if num % 2 == 1:
            odd = True
            break

    max_num = max(S)
    n = int(max_num / 2)

    if max_num % 2 == 0:
        if odd:
            return (n + 1)
        else:
            return n
    else:
        return n + 1
