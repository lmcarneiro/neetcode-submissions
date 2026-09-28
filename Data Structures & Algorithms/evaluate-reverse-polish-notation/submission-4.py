class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        numStack = []
        ops = ["+", "-", "*", "/"]

        for c in tokens:
            print(numStack)
            if c not in ops:
                numStack.append(int(c))
            else:
                if numStack:
                    a = numStack.pop()
                    b = numStack.pop()
                    if c == "+":
                        res = b + a
                    elif c == "-":
                        res = b - a
                    elif c == '*':
                        res = b * a
                    else:
                        res = int(float(b) / a)
                numStack.append(res)
        return numStack[0]


