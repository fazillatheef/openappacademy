letters = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7": "pqrs", "8":"tuv", "9": "wxyz"}
def letterCombinations( digits: str):
    combos = []
    def rec(i, combo):
        if(len(combo) == len(digits)):
            combos.append(combo)
            return
        for num in digits[i]:
            for letter in letters[num]:
                combo += letter
                rec(i+1,combo)
                combo = combo[:-1]
    if(len(digits)):
        rec(0, "")    
    return combos

print(letterCombinations('456'))