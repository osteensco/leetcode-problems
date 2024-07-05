# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8





class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # open parens can be added when open = close and 
        # open are still available, or open > close.
        # close paren can never be more than open !(open < close).
        # so really as long as open is < n open can be added

        # close paren can only be added when open > close
        
        # check if we used all parentheses and they equal, 
        # and add to result 

        validParen = ""
        result = []

        def recursivelyGen(openCnt, closeCnt, validParen):

            # for each condition, we are creating a new branch in a tree
            # we after our recursive call we essentially backtrack up to the 
            # previous node by removing the last addition to the string
            # whiteboard desc https://www.youtube.com/watch?v=s9fokUqJ76A
            if openCnt < n:
                validParen = concat(validParen, "(")
                recursivelyGen(openCnt+1, closeCnt, validParen)
                validParen = validParen[:-1]

            if openCnt > closeCnt:
                validParen = concat(validParen, ")")
                recursivelyGen(openCnt, closeCnt+1, validParen)
                validParen = validParen[:-1]

            if openCnt == n == closeCnt:
                result.append(validParen)
                return

        recursivelyGen(0,0, validParen)
        return result
        
        
