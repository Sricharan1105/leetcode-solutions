# Problem   : Running Sum of 1d Array
# Difficulty : Easy
# Link      : https://leetcode.com/problems/running-sum-of-1d-array/
# Date      : 16-May-2026

# Time  : O(n)
# Space : O(1)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for i in nums:
            
            total = total + i
            result.append(total)
        return result
