def find_median(nums1,nums2):
    m = len(nums1)
    n = len(nums2)
    mmax = m
    nmax = n
    mid = int((m+n)/2)
    odd = (m+n)%2
    m1 = 0
    n1 = 0
    current = 0.0
    median = 0.0
    print(f'mid : {mid}, odd : {odd}')
    
    for i in range(m+n):
        if m1 < mmax and n1 < nmax:
            if nums1[m1] < nums2[n1]:
                current = nums1[m1]
                m1 += 1
            elif nums2[n1] < nums1[m1]:
                current = nums2[n1]
                n1 += 1
            else:
                current = nums1[m1]
                m1 += 1
        else:
            if m1 < mmax and n1>= nmax:
                current = nums1[m1]
                m1 += 1
            elif n1 < nmax and m1>= mmax:
                current = nums2[n1]
                n1 += 1
            else:
                break
        print(f'current : {current}, i :{i}, n1 : {n1}, m1 : {m1}')
        if odd:
            if i == mid:
                median = current
                break
        else:
            if i == mid   or i == mid -1:
                print("here")
                median += current /2.0
                if i == mid + 1:
                    break
    return median
#print(find_median([1,2],[3]))
#print(find_median([1,2,3],[]))
print(find_median([1,2],[3,4]))