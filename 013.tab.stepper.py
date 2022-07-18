# Solution in the website seems wrong. Not sure how it passed the test
# For the given array input. Make steps based on the numbers in the array
# If you are able to reach the end then return True
# :Tabulation solution:
def stepper(steps):
    ls = len(steps)
    tab_steps = [False] * ls
    tab_steps[0] = True
    for i in range(ls):
        steps_to_take = min(i + steps[i] + 1 ,ls)
        if tab_steps[i]:
            for j in range(i, steps_to_take):
                tab_steps[j]=True
    return tab_steps[ls-1]

print(stepper([1,2,3])) #True
print(stepper([1,2,1,0,1])) #False
print(stepper([1,2,1,1,1])) #True
print(stepper([3,1,0,5,10])) #True
print(stepper([3,4,0,1,10])) #True
print(stepper([2,3,1,1,0,4,7,8])) #False