# This code is finding unique combination of coins to make up an amount
# To do that it has to try number of different coins
# The path is counted when the amount becomes zero
def maxUniqueCoin(deno,amt,memo={}):
    key= str(deno)+"-"+str(amt) 
    if  key in memo:
        return memo[key]
    if amt== 0:
        return 1
    if len(deno) == 0:
        return 0
    current_coin = deno[0]
    total = 0
    num = 0
    while num*current_coin <= amt:
        total += maxUniqueCoin(deno[1:],amt-num*current_coin,memo) 
        num += 1
    memo[key]=total
    return total

print(maxUniqueCoin([1,2,3,4,5],50))