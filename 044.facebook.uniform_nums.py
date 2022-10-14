def getUniformIntegerCountInInterval(A, B):
    def tozero(num):
        s_num = str(num)
        len_num = len(s_num)
        first_num = int(s_num[0])
        all_same = 1
        for c in s_num:
            if int(c) < first_num:
                all_same = 0
                if first_num == 1:
                    first_num = 9
                    len_num -= 1
                else:
                    first_num = first_num - 1
                break
            elif int(c) > first_num:
                all_same = 0
                break
            else:
                continue
        return (len_num - 1)*9 + first_num, all_same
    to_B, s2 = tozero(B)
    to_A, s1 = tozero(A)
    s = 0
    if s1 == 1 or s2 == 1:
        s = 1
    print(to_B, to_A)
    return to_B - to_A + s 


print(getUniformIntegerCountInInterval(1, 9))
print(getUniformIntegerCountInInterval(75, 300))
print(getUniformIntegerCountInInterval(50, 50))
print(getUniformIntegerCountInInterval(999999999999, 999999999999))
