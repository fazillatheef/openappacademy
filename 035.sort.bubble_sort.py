lis = [4,7,2,8,3,6,9,1,5]

def bubble_sort(li):
    def swap(i,j):
        temp = li[j]
        li[j] = li[i]
        li[i] = temp
    array_len = len(li)
    swapped = True
    while swapped:
        swapped = False
        for i in range(array_len):
            if i + 1 == array_len:
                break
            if li[i] > li[i+1]:
                swap(i,i+1)
                swapped = True
        array_len -= 1
    
    return li

print(bubble_sort(lis))