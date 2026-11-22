class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        q = deque()
        for i, c in enumerate(s):
            q.append((i, c))
            h[c] = 1 + h.get(c, 0)

        while q:
            i, c = q.popleft()
            if h[c] == 1:
                return i

        return -1