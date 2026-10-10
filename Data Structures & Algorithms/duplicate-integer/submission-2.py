class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        saved = set()
        for n in nums:
            if n in saved:
                return True
            saved.add(n)
        return False