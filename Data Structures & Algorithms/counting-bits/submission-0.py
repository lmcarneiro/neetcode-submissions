class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]*(n + 1)
        for i in range (n + 1):
            b = bin(i)
            count = 0
            for j in b[2:]:
                print(f"j {j} and {j == '1'}")
                if j == '1':
                    count += 1
            output[i] = count
        return output