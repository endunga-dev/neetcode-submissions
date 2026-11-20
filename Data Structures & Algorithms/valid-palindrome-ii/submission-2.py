class Solution:
    def validPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else: # Splicing excludes end, so for R dont need -1
                if s[L+1:R+1] == "".join(reversed(s[L+1:R+1])) or s[L:R] == "".join(reversed(s[L:R])):
	                return True
                else:
                    return False
        return True

                    