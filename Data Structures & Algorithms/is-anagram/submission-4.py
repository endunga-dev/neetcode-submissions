class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        # First loop
        for char in s:
            if not char in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        # Second loop
        for char in t:
            if not char in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1
        # Compare dicts
        if not s_dict == t_dict:
            return False
        return True