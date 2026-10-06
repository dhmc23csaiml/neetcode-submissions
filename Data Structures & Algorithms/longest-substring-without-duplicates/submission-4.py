class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        le=set()
        left=0
        max_length=0
        for i in s:
            while i in le:
                le.remove(s[left])
                left+=1
            le.add(i)
            max_length=max(max_length,len(le))
        return max_length
        