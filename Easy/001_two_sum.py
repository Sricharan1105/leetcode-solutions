# Problem   : Two Sum
# Difficulty : Easy
# Link      : https://leetcode.com/problems/two-sum/
# Date      : 17-May-2026

# Approach: Hashmap
# Time  : O(n)
# Space : O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]
            
            if need in seen:
                return [seen[need],i]

            seen[nums[i]] = i
