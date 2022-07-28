# Regular expression implementation for * and .
# s1-alpha-s2
# s1-.-s2
# s2-*-s3
# Not working
class alpha:
    def __init__(self,ch,next=None):
        self.state = "alpha"
        self.ch = ch
        self.next = next
    def check(self,s):
        if len(s)==0:
            return False
        if s[0] == self.ch:
            if self.next != None:
                return self.next.check(s[1:])
        else:
            return False
class dot:
    def __init__(self,next=None):
        self.state = "dot"
        self.next = next
    def check(self,s):
        if len(s)==0:
            return False
        c = s[0]
        if (c >='A' and c<='Z') or (c >='a' and c<='z'):
            if self.next != None:
                return self.next.check(s[1:]) 
        else:
            return False

class star:
    def __init__(self,previous=None,next=None):
        self.state = "star"
        self.previous = previous
        self.next = next
    def check(self,s):
        if s == "":
            return self.next.check(s)
        return self.previous.check(s)
class term:
    def __init__(self):
        self.state = "term"
        self.next = None
    def check(self,s):
        if s == "":
            return True
        else:
            return False
class start:
    def __init__(self,next=None):
        self.next = next 

def check_reg(s:str,p:str) -> bool:
    current = start()
    reg = current
    previous = None
    for c in p:
        if c=='.':
            previous = current
            current = dot()
            previous.next = current
        elif c=='*':
            previous = current
            current = star(previous=previous)
            previous.next = current
        else:
            previous = current
            current = alpha(c)
            previous.next = current
    current.next = term()
    current = reg.next
    return current.check(s)

print("1",check_reg("aa",".."))
print("2",check_reg("ab","a."))
print("3",check_reg("abc","a."))
print("4",check_reg("abc","a.c"))
print("5",check_reg("abc",""))
print("6",check_reg("","a."))
print("7",check_reg("abc","c.*"))
print("7",check_reg("abc",".*"))


    
        