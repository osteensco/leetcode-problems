class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:



        # O(n) time complexity, using a hashmap or a set - worst case scenario iterates through entire list once
        # O(n) memory usage

        hash = set()
        # hash = {}
        for n in nums:
            if n in hash:
                return True
            else:
                hash.add(n)
                # hash[n] = n
        return False



        # create a set and compare lengths
            # a set only contains unique values and is hashable
            # the process of creating a set iterates through the entire list every time,
            # so the worst case scenario is every scenario making this solution less optimal 
            # even though it has the same time complexity and memory usage. 
        # O(n) time complexity but is slightly faster than above solution (at least for python)
        # O(n) memory usage 

        # return len(nums) != len(set(nums))



        # # brute force method
        # # this method checks all remaining values in the list 
        # O(n^2) time complexity because for the nested loop
        # O(1) because no copy of the data is created

        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        #         else:
        #             continue
        # return False



