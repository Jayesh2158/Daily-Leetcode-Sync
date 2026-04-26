class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_contain = float()
        i, j = 0, len(height) - 1
        while i < j:
            max_contain = max(max_contain, abs(i - j) * min(height[i], height[j])) 
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return int(max_contain)