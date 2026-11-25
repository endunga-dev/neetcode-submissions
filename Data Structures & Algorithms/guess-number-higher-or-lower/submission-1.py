# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        mid = (low + high) // 2
        # Quick check if n is the mystery number
        if guess(n) == 0:
            return n
        else: # Otherwise keep using mid
            while low < high:
                if guess(mid) == 0:
                    return mid
                elif guess(mid) == -1:
                    high = mid # our new high is mid, and our new mid is the mid between low and old mid
                    mid = (low + high) // 2
                elif guess(mid) == 1:
                    low = mid # opposite of first comment
                    mid = (low + high) // 2
        return mid 
        # Return mid so None is never returned and if low == high we return last number