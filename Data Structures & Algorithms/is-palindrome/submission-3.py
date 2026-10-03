class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=s.lower()
        a="".join(char.lower() for char in s if char.isalnum())
        print(a)
        print(a[::-1])
        return a==a[::-1]
        
        