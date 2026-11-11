class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        init_color = image[sr][sc]

        def dfs(r, c):
            if (r >= rows or c >= cols or
                r < 0 or c < 0 or
                image[r][c] != init_color):
                return

            image[r][c] = color
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
        
        if init_color != color:
            dfs(sr, sc)

        return image