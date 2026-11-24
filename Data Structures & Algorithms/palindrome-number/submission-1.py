class Solution:
    def isPalindrome(self, x: int) -> bool:
        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            if x // div != x % 10:
                return False
            
            x = (x % div) // 10
            div = div // 100

        return True