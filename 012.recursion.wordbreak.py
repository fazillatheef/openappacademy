# Check if a string can be made by just using the words in the provided dict
# My try of wordbreak using recursion
def wordbreak(words,s,memo={}):
    if s in memo.keys():
        return memo[s]
    if len(s)==0:
        return True
    for w in words:
        wl = len(w)
        if w == s[:wl]:
            memo[s] = wordbreak(words,s[wl:],memo)
            if memo[s]:
                return memo[s]
    return False

print(wordbreak(['pen','apple','ap','sa'],"pensaapplepenap")) # should be True
print(wordbreak(['cat','and','dog'],"catandog")) # should be False
print(wordbreak(['cat','and','an','dog'],"catandog",{})) # should be True