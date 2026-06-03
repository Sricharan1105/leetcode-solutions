class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ""
        

        for ch in s:
            if ch.isalnum():
                rev += ch.lower()

        return rev == rev[::-1]
