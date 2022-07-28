# Roman to int
def romanToInt( s: str) -> int:
    l_s = len(s)
    num = 0
    roman = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900,'M':1000,'D':500,'C':100,'L':50,'V':5,'X':10,'I':1}
    i = 0
    for k in range(l_s):
        if i >= l_s:
            break
        if i + 1 < l_s:
            if s[i:i+2] in roman.keys():
                num += roman[s[i:i+2]]
                i += 2
                continue
        if s[i] in roman.keys():
            num += roman[s[i]]
        i += 1
        
    return num

print(romanToInt('CCXIV'))