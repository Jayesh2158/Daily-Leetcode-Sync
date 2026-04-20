class Solution:
    def two_sum_closest(self, nums, target):
        nums.sort()
        left, right = 0, len(nums) - 1
        
        closest_sum = float('inf')
        result = []
        
        while left < right:
            curr_sum = nums[left] + nums[right]
            
            # Update closest sum
            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum
                result = [nums[left], nums[right]]
            
            # Move pointers
            if curr_sum < target:
                left += 1
            else:
                right -= 1
        
        return result
