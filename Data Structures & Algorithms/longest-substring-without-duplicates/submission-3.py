class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        le = set()
        print(le)
        max_len = 0
        left = 0
        
        for i in s:
            while i in le:
                le.remove(s[left])
                left += 1
            le.add(i)
            max_len = max(max_len, len(le))
        return max_len