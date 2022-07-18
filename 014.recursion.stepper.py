# Solution in the website seems wrong. Not sure how it passed the test
# For the given array input. Make steps based on the numbers in the array
# If you are able to reach the end then return True
# :Recursion:
def stepper(steps,memo={}):
    if len(steps)==0:
        return True
    for i in steps:
        if i==0:
            break
        if stepper(steps[i:]):
            return True
    return False

print(stepper([1,2,1,0,1])) #False
print(stepper([1,2,1,1,1])) #True
print(stepper([3,1,0,5,10])) #True
print(stepper([3,4,0,1,10])) #True
print(stepper([2,3,1,1,0,4,7,8])) #False