class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        # First loop
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        # Second loop
        for num_count in num_dict.values():
            # Will return true if any number has a value greater than one, or appears more than once
            if num_count > 1:
                return True
            else:
                continue
        return False
        