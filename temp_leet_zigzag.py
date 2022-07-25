def convert(s: str, numRows: int) -> str:
    L = len(s)
    res = ""
    if L == 1 or numRows ==1:
        return s
    period = 2 * (numRows -1)
    for i in range(numRows):
        step = period - 2 * i
        for j in range(i,L,period):
            res+=s[j]
            if 0<step<period and j+step < L:
                res+=s[j+step]
    return res
 
print(convert("PAYPALISHIRING",3)) #"PAHNAPLSIIGYIR"
