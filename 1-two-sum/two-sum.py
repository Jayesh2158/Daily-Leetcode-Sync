class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            temp = target - num
            if temp in d:
                return [d[temp], i]
            d[num] = i