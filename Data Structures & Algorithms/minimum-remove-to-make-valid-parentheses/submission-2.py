class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack:
                    remove.append(i)
                    continue
                else:
                    stack.pop()
        remove += stack
        chars = list(s)
        for i in reversed(remove):
            chars.pop(i)
        return "".join(chars)