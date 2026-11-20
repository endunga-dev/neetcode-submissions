class Solution:
    def isPalindrome(self, s: str) -> bool:      
        L, R = 0, len(s) - 1
        while L < R:
            # Increment L until we have a valid char
            while L < R and not s[L].isalnum():
                L += 1
            # Do the same to R
            while L < R and not s[R].isalnum():
                R -= 1
            # Check now
            if s[L].lower() == s[R].lower():
                L += 1
                R -= 1
                continue
            else:
                return False
        return True