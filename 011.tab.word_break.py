# Check if a string can be made by just using the words in the provided dict
# Table is bigger than the string by one byte. The end of a word is marked True. Then try other words
# starting from the last found position. repeat this for all newly found word positions.
# Then if the last position in the table is True it means the words can be used to create the string.
def wordbreak(words,s):
    table = [False] * (len(s) + 1)
    table[0] = True
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if table[i] == True:
                if s[i:j] in words:
                    table[j]=True
    return table[-1]

print(wordbreak(['pen','apple'],"penapplepen")) # should be True
print(wordbreak(['cat','and','dog'],"catandog")) # should be False