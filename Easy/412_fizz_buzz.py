# Problem   : Fizz Buzz
# Difficulty : Easy
# Link      : https://leetcode.com/problems/fizz-buzz/
# Date      : 15-May-2026

# Time  : O(n)
# Space : O(n)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else :
                result.append(str(i))
        return result
        