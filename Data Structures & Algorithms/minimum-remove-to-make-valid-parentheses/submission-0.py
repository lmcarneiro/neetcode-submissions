class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = []
        res = ""
        for i, c in enumerate(s):
            print(i, c, stack, remove)
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack:
                    remove.append(i)
                    continue
                else:
                    stack.pop()
        print(remove)
        remove += stack
        print(remove)
        chars = list(s)
        for i in reversed(remove):
            chars.pop(i)
        res = "".join(chars)
        return res