class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())
        print(s)
        print(s[:len(s)//2])
        print(s[len(s)//2 + 1:][::-1])
        print(s[:len(s)//2] == s[len(s)//2 + 1:][::-1])
        if len(s) % 2 == 1 and s[:len(s)//2] == s[len(s)//2 + 1:][::-1]:
            return True
        if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:][::-1]:
            return True
        return False