# Function checks for impossible denominations
def checkMinChange(deno,amt):
    for coin in deno:
        if amt % coin == 0:
            return minChange(deno,amt,{})
    else:
        return None

# Function takes two inputs - arrary with different denominations & Target amount
# Should return the minimum number of coins needed
# Each time a recursive call is done 1 is added
# The final sum is stored in a an array
# The minimum sum is returned
def minChange(deno,amt,memo={}):
    if amt in memo:
        return memo[amt]
    if amt == 0 :
        return 0
    num_coins=[]
    for coin in deno:
        if coin <= amt:
            num_coins.append(minChange(deno,amt-coin,memo) +1)
    memo[amt] = min(num_coins)
    return memo[amt]

print(checkMinChange([1,2],3))
print(checkMinChange([1,2,5],20))
print(checkMinChange([1,3,5],4))
print(checkMinChange([20],100))
print(checkMinChange([2,4],7))
