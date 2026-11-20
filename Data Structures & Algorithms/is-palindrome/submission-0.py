class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(char for char in s if char.isalnum()).lower()
        reversed_s = "".join(reversed(clean_s))
        return clean_s == reversed_s