from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0
        answer = float('-inf')

        for i, num in enumerate(nums, 1):
            prefix += num
            remainder = i % k

            if min_prefix[remainder] != float('inf'):
                answer = max(
                    answer,
                    prefix - min_prefix[remainder]
                )

            min_prefix[remainder] = min(
                min_prefix[remainder],
                prefix
            )

        return answer
