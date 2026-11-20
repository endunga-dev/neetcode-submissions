class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    final.append(i)
        return final