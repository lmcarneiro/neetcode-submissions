class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # res = 0

        while True:
            # res += 1
            l, r = 0, 1
            while r < len(s):
                if s[l] == s[r]:
                    if r - l == k - 1:
                        s = s[:l] + s[r + 1:]
                        break
                else:
                    l = r
                r += 1
            # print(res, l, r, len(s), s)
            if r >= len(s):
                break

        return s
        