def generateParenthesis(n: int):
    stack = []
    powerset = []
    def dfs(openb: int, closeb: int) -> None:
        if openb == 0 and closeb == 0:
            powerset.append("".join(stack))
            return
        if openb != 0:
            stack.append("(")
            dfs(openb - 1, closeb)
            stack.pop()
        if openb < closeb:
            # We used more open brackets then close brackets
            stack.append(")")
            dfs(openb, closeb - 1)
            stack.pop()

        
    dfs(n, n)
    return powerset

print(generateParenthesis(5))