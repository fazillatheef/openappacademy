def commonpre(strs):    
    result = strs[0]
    for i in strs:
        while not i.startswith(result):
            result = result[:-1]
            
    return result

print(commonpre(['fazil','farha','fariza']))