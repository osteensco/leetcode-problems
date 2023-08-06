# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 







class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #need to use a hashmap to keep a count of each number and how often it appears
        #in order to generate an ordered list by count, use an array of arrays and insert a given number at the index of it's count.
            #as a result higher frequency numbers will be located towards the end of the array
        mp = {}
        tracker = [[] for i in nums]+[[]]

        for n in nums:
            if n in mp:
                mp[n] += 1
            else:
                mp[n] = 1
        
        for n, c in mp.items():
            tracker[c].append(n)    

        mx = []
        for i in range(len(tracker)-1, 0, -1):
            mx += tracker[i]
            if len(mx) == k:
                return mx

