class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}

        for num in nums:
            if num in counts:
                return True
            else:
                counts[num] = 1

        return False
