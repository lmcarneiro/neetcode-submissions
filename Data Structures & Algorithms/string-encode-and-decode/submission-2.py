class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s))
            encoded += '#'
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        print(s)
        while i < len(s):
            num = ''
            while s[i] != '#':
                num += s[i]
                i += 1
            print(num)
            i += 1
            j = i + int(num) - 1
            print(f"i, j {i}, {j}, {s[i:j+1]}")
            strs.append(s[i:j+1])
            i = j + 1
        return strs


