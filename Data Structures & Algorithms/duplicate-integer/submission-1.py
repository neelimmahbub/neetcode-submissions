class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count: int = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        if (count - len(nums)) >= 2:
            return True
        else:
            count = 0

        return False
        