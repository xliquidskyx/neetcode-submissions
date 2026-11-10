class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prevSet = set()
        maxStr = 0
        l = 0
        for r in range(len(s)):
            while s[r] in prevSet:
                prevSet.remove(s[l])
                l += 1
            prevSet.add(s[r])
            maxStr = max(maxStr, len(prevSet))
        return maxStr
