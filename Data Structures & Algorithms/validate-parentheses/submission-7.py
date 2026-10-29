class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            "]": "[",
            "}": "{",
            ")": "(",
        }

        for c in s:
            if c in brackets.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                bracket = stack.pop()
                if brackets[c] != bracket:
                    return False

        return not stack