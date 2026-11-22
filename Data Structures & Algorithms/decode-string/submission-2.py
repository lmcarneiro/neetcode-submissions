class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0

        def dfs():
            res = ""
            k = 0

            while self.i < len(s):
                c = s[self.i]

                if c.isdigit():
                    k = k * 10 + int(c)
                elif c == "[":
                    self.i += 1
                    res += k * dfs()
                    k = 0
                elif c == "]":
                    return res
                else:
                    res += c
                
                self.i += 1
            return res
        return dfs()