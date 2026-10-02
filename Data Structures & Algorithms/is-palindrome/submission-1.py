class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(ch.lower() for ch in s if ch.isalnum())
        a=list(s)
        print(a)
        print(a[::-1])
        return a==a[::-1]
        
        