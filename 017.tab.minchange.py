# Accepts an array of coins and and amount. Determine the minimum amount of coins required to make the amount
# Use tabulation

# Data structure here is an array for each amount until the actual amount
# High value is stored intially - this avoids the need to have another array to indicate
# if certain amount is possible with denominations that are checked 

# The algorithm finds the multiples of each denomination for all values until the actual amount,
#  if a certain denomination is not able to produce an amount
# then it checks if the reminder can be made using other denominations. 
# Store only the minimum possible attempts

import math
def minchange(deno,amount):
    tab = [math.inf] * (amount + 1)
    tab[0] = 0

    for val in deno:
        for amt in range(amount + 1):
            qty = 0
            while (qty * val) <= amt:
                remainder = amt - qty * val
                attempt =  qty + tab[remainder]
                if attempt < tab[amt]:
                    tab[amt] = attempt
                qty += 1
    return tab[-1]

print(minchange([5,2,1],11)) # 3
print(minchange([4,5],8)) # 2
print(minchange([1,5,10,25],15)) # 2
print(minchange([1,5,10,25],100)) # 4
