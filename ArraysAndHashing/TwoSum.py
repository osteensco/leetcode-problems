# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # O(n) time complexity
        # O(n) memory usage
        numsdict = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in numsdict:
                return [i, numsdict[diff]]         
            else:
                numsdict[v] = i



    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     # O(n^2) time complexity
    #     # O(1) memorary usage
    #     for i in range(len(nums)-1):
    #         diff = target - nums[i]
    #         print(diff)
    #         try:
    #             idx = nums.index(diff,i+1)
    #             return [i, idx]               
    #         except ValueError:
    #             continue   

