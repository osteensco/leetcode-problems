# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.



class Solution:


    # hashmap comparison
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def count_chars(strng):
            chars = {}
            for l in strng:
                if l not in chars:
                    chars[l] = 1
                else:
                    chars[l] += 1
            return chars
        #could be optimized further by using a single loop instead of multiple
        s_hash = count_chars(s)
        t_hash = count_chars(t)

        for k in s_hash.keys():
            try:
                if s_hash[k] == t_hash[k]:
                    continue
                else:
                    return False
            except KeyError:
                return False
        return True


    # # using a merge sort

    # def isAnagram(self, s: str, t: str) -> bool:

    #     return self.merge_sort_string(s) == self.merge_sort_string(t)

    # def merge_sort_string(self, st):

    #     if len(st) <= 1:
    #         return st

    #     middle = len(st) // 2
    #     left_half = st[:middle]
    #     right_half = st[middle:]

    #     left_sorted = self.merge_sort_string(left_half)
    #     right_sorted = self.merge_sort_string(right_half)

    #     return self.merge(left_sorted, right_sorted)


    # def merge(self, left, right):
    #     merged = []
    #     left_index, right_index = 0, 0

    #     while left_index < len(left) and right_index < len(right):
    #         if left[left_index] < right[right_index]:
    #             merged.append(left[left_index])
    #             left_index += 1
    #         else:
    #             merged.append(right[right_index])
    #             right_index += 1

    #     merged.extend(left[left_index:])
    #     merged.extend(right[right_index:])

    #     return ''.join(merged)





    # # using built in sort
    

    # def isAnagram(self, s: str, t: str) -> bool:
        # s = list(s)
        # t = list(t)
        
        # s.sort()
        # t.sort()
        
        # s = "".join(s)
        # t = "".join(t)
        
        # return t == s










