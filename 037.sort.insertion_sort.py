a = [5, 7, 100, 2, 4, 8, 7, 1, 3]


def insertion_sort(a):
    for i in range(1, len(a)):
        curr = a[i]
        for j in range(i-1, -1, -1):
            if curr > a[j]:
                break
            a[j+1] = a[j]
        else:
            j -= 1
        a[j+1] = curr
    return a


def insertion_sort1(a):
    len_a = len(a)
    for i in range(1, len_a):
        pos = i
        for j in range(i):
            print(i, i-j-1, a[i], a[i-j-1], a)
            if a[pos] < a[i-j-1]:
                temp = a[pos]
                a[pos] = a[i-j-1]
                a[i-j-1] = temp
                pos = i-j-1
            else:
                break
    return a


print(insertion_sort(a))
