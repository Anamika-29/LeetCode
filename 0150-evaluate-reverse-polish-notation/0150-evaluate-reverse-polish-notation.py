class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        while len(tokens) > 0:
            toke = tokens.pop(0)
            if toke == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(second+first)
            elif toke == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second-first) # The order of numbers is important
            elif toke == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(second*first)
            elif toke == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(float(second)/first)) # evaluates to a 0 with the 6/-132 scenario (as required).
            else:
                stack.append(int(toke))
        return stack.pop()