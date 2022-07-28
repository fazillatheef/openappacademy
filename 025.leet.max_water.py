# Maximum water that can be filled between two values in an array
# Height is the actual value and distance between the indexes is the width
def maxArea(height) -> int:
    le= len(height)
    max_v = 0
    i = 0 
    j = le - 1
    while i != j:
        max_v = max(max_v,min(height[i],height[j])*(j-i))
        if height[i] > height[j]:
            j-=1
        else:
            i+=1
    return max_v