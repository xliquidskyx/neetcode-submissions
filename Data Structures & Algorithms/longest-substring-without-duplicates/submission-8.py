class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l = 0
        subset = set()
        for r in range(len(s)):
            while s[r] in subset:
                subset.remove(s[l])
                l += 1
            subset.add(s[r])
            maxLength = max(len(subset), maxLength)
        return maxLength
        