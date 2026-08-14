class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for item_1 in nums:
            if item_1 in seen:
                return True
            seen.add(item_1)
        return False