# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105








class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        # 3sum is much simpler to solve with a sorted array
        nums.sort()
        # we set our initial base, and then use two pointers in the rest of the array
        i = 0
        
        # our base really only needs to be negative ints or 0, since we our total sum should equal 0
        while i < len(nums)-1 and nums[i] <= 0:
            # to avoid duplicates we increment our iterator if we are on the same value as the previous iteration
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            # our pointers will essentially look in the sub array of nums[i+1:]
            l = i + 1
            r = len(nums)-1
            
            # same algorithm as twoSumII (almost)
            while l < r:
                
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    # we may still have other valid solutions from this base (nums[i])
                    # so we iterate our left pointer
                    l += 1
                    # however, to avoid duplicates, if the value of our left pointer is now the same as the previous one we want to keep iterating
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

            i += 1

        return result
