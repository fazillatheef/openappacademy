# check if brackets match
# []{}() returns False
# [{}]() returns False
# [()](){[} returns False
def matchbr1(s):
    stack =[]
    brackets = {"[":"]","(":")","{":"}"}
    for c in list(s):
        if c in brackets.keys():
            stack.append(c)
        elif c in brackets.values():
            if brackets[stack[-1]] == c:
                stack.pop()
            else:
                return False
        else:
            return False
    return True 

print(matchbr('[]{}()'))
print(matchbr('[{}]()'))
print(matchbr('[()](){[}'))
print(matchbr(''))
print(matchbr('asda'))
print('({}P}{()',matchbr('({}P}{()'))