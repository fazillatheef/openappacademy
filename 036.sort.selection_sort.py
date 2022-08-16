a = [5,7,100,2,4,8,7,1,3]

def selection_sort(a):
    len_a = len(a)
    for i in range(len_a):
        min = i
        for j in range(i+1,len_a):
            if a[j] < a[min]:
                min = j
        temp = a[i]
        a[i] = a[min]
        a[min] = temp
    return a

print(selection_sort(a))