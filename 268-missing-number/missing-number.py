class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # hanannur
        full=set(range(len(nums)+1))
        num_set=set(nums)
        missing=full-num_set
        return missing.pop()
    