# Find max sum of non adj numbers in an array
def maxsumadj(nums):
    len_num = len(nums)
    tab = [0] * len_num
    for i in range(len_num):
        for j in range(i,len_num):
            if j > i + 1:
                tab[j] = max(tab[j],nums[i]+nums[j],tab[i] + nums[j])
    return tab[len_num - 1]


def maxsumadj1(nums):
    if len(nums) == 0:
        return 0
    len_num = len(nums)
    tab = [0] * len_num
    tab[0] = nums[0]
    for i in range(1,len_num):
        tab[i] = max((tab[i-2] if i > 1 else 0) + nums[i],tab[i-1])
    return tab[len_num - 1]

print(maxsumadj([2,7,9,3,4])) # 15
print(maxsumadj([4,2,1,6])) #10
print(maxsumadj1([2,7,9,3,4])) # 15
print(maxsumadj1([4,2,1,6])) #10

"""
2   7   9    3   4
2   7
2   7   11   
2   7   11   11
2   7   11   11  15

4   2   1  6
4   4
4   4   5
4   4   5  10
"""