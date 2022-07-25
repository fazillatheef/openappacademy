from tkinter import W


def maxsubstring(s):
    i = 0
    start = 0
    len_string = len(s)
    if len_string==1:
        return 1
    current_string = {}
    max_len =0
    endpos = 0
    for i in range(len_string):
        if s[i] in current_string.keys():
            start = max(start,current_string[s[i]] + 1)
        endpos = i
        current_string[s[i]] = i
        print(s[:i+1],current_string,start,endpos) 
        if  endpos - start + 1  > max_len:
            max_len = endpos - start  +1
    return max_len 

print(maxsubstring("abcabcbb"))
print(maxsubstring("bbbbb"))
print(maxsubstring("au"))
print(maxsubstring("pwwkew"))
print(maxsubstring("abba"))