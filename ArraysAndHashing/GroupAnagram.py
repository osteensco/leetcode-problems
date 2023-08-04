# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.







class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        mp = {}
        
        for s in strs:
            # init a vector to track letter counts
            vec = [0] * 26
            for l in s:
                # map the letter to the correct index in our vector count and increment
                idx = letter.index(l)
                vec[idx] += 1
            # once the vector is finalized convert to tuple which is immutable and can be a key in a dictionary unlike a list which is mutable
            vec = tuple(vec)
            if vec in mp:
                mp[vec].append(s)
            else:
                mp[vec] = [s]
        
        return [mp[k] for k in mp.keys()]








