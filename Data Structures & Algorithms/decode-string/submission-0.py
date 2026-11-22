class Solution:
    def decodeString(self, s: str) -> str:
        char_stack = []
        num_stack = []
        res = ''
        k = 0

        for i, c in enumerate(s):
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                char_stack.append(res)
                num_stack.append(k)
                res = ""
                k = 0
            elif c == "]":
                temp = res
                res = char_stack.pop()
                times = num_stack.pop()
                res += temp * times
            else:
                res += c
                
        return res

                