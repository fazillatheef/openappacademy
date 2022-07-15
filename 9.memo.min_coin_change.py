# Function takes two inputs - arrary with different denominations & Target amount
# Should return the number of coins needed
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

print(minChange([1,2],3,{}))
print(minChange([1,2,5],20,{}))
print(minChange([1,3,5],4,{}))
print(minChange([20],100,{}))
print(minChange([2,4],7,{}))
