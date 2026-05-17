# Problem   : Palindrome Number
# Difficulty : Easy
# Link      : https://leetcode.com/problems/palindrome-number/
# Date      : 13-May-2026

# Approach: Convert to string and reverse
# Time  : O(n)
# Space : O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        rev = ""
        for i in range(len(x)-1, -1, -1):
            rev = rev + x[i]
            
        return x == rev