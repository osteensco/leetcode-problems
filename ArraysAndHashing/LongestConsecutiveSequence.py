# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109





class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(nums)
        length = 0
        currlen = 0
        for i in range(len(nums)):
            if i == 0:
                currlen += 1   
            elif nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1]+1:
                currlen += 1
            elif currlen >= length:
                length = currlen
                currlen = 1
            else:
                currlen = 1
        if currlen > length:
            length = currlen

        
        return length
                


# without sorting
        nums = set(nums)
        length = 0
        for i in nums:
            if i-1 not in nums:
                currlen = 0
                while i+currlen in nums:
                    currlen += 1
                if currlen >= length:
                    length = currlen
                else:
                    currlen = 0
        
        return length

