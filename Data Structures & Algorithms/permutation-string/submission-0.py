class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1 = sorted(s1)

        for l in range(len(s2)):
            r = l + len(s1)
            print(s1)
            print(s2[l:r])
            if s1 == sorted(s2[l:r]):
                return True
        
        return False