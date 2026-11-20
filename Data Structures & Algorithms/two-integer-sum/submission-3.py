class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index, value in enumerate(nums):
            # Map every index to the number in question in the array
            dictionary[value] = index 
        # Second for loop but not O(n^2) time complexity since it isnt nested
        for index, value in enumerate(nums): 
            # Our desired number for the 2 sum is the target number minus whatever number we are currently on
            desired = target - value 
            # Checks if that number is in the dict and if its at the right index/pos
            if desired in dictionary and dictionary[desired] != index: 
                return [index, dictionary[desired]]