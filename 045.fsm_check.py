#!/usr/bin/python3
# Lets try to check the following regular expression
# r"aa+b+a1"
edges = {
    (1,'a'):2,
    (2,'a'):3,
    (3,'a'):3,
    (3,'b'):4,
    (4,'b'):4,
    (4,'a'):5,
    (5,'1'):6
}
accepting = [6]

def fsmsim(input,current,edges,accepting):
    if input == "":
        if current in accepting:
            return True
        else:
            return False
    
    next_state = (current,input[0])
    if next_state in edges.keys():
        current = edges[next_state]
        return fsmsim(input[1:],current,edges,accepting)
    else:
        return False

print(fsmsim("aabaa1",1,edges,accepting))
print(fsmsim("aabbbba1",1,edges,accepting))
print(fsmsim("aaaa1",1,edges,accepting))
print(fsmsim("aaaabba1",1,edges,accepting))
print(fsmsim("aabaa1",1,edges,accepting))
print(fsmsim("aabbbbba1",1,edges,accepting))
print(fsmsim("aaaaaaaaaabbbbba1",1,edges,accepting))
print(fsmsim("abbbbba1",1,edges,accepting))

    
