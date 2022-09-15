def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    ct = 0
    for i in range(N):
        if C[i] == 'P':
            for pa in range(X, Y+1):
                if i + pa > N-1:
                    break
                if C[i+pa] == 'A':
                    for ab in range(X, Y+1):
                        if i + pa + ab > N-1:
                            break
                        if C[i+pa+ab] == 'B':
                            ct += 1
        elif C[i] == 'B':
            for pa in range(X, Y+1):
                if i + pa > N-1:
                    break
                if C[i+pa] == 'A':
                    for ab in range(X, Y+1):
                        if i + pa + ab > N-1:
                            break
                        if C[i+pa+ab] == 'P':
                            ct += 1
    return ct


print(getArtisticPhotographCount(5, 'APABA', 1, 2))
print(getArtisticPhotographCount(8, '.PBAAP.B', 1, 3))
