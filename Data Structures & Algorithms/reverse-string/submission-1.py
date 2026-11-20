class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L, R = 0, len(s) - 1
        while L < R:
            left = s[L]
            right = s[R]
            s[L] = right
            s[R] = left
            L += 1
            R -= 1