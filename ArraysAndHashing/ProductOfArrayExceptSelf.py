# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)








class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        

# requires two passes of the nums array
# moving forward, the prefix starts at 1. the prefix is essentially all items to the left of the current index multiplied together.
# since there is nothing to the left at the first iteration, the prefix starts at 1 (same idea for the postfix).
# the prefix is added to the solution array. the prefix is then multiplied by the current iteration of the index of the nums array.
# loop until complete.

# moving backwards, the postfix starts at 1. the postfix is then multiplied by the current iteration of the index in the solution array.
# the postfix is then multiplied by the current iteration of the index of the nums array.
# loop until complete.

# once second loop is complete, we have our solution.



        sol = []
        prefix = 1
        for x in range(len(nums)):
            if x-1 < 0:
                ans = 1
                
            else:
                ans = prefix
            
            sol.append(ans)
            prefix *= nums[x]
        
        
        postfix = 1
        for y in range(len(nums)-1, -1, -1):
            if y+1 > len(nums)-1:
                ans = 1

            else:
                ans = postfix
            
            sol[y] *= ans
            postfix *= nums[y]

        return sol
    

