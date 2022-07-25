# Find max sum of non adj numbers in an array
# using recursion
def maxsumadj(nums,memo=None):
    if memo is None:
        memo={}
    len_num = len(nums)
    if len_num in memo:
        return memo[len_num]
    if len_num == 0:
        return 0
    if len_num == 1:
        return nums[0]
    
    memo[len_num] = max(nums[0]+maxsumadj(nums[2:]),nums[1])
    return memo[len_num]

print(maxsumadj([2,7,9,3,4])) # 15
print(maxsumadj([4,2,1,6])) #10

