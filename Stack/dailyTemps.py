# 739. Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100




# better version https://www.youtube.com/watch?v=cTBiBSnjO3c

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # initialize the returned list, default values to 0
        res = [0]*len(temperatures)
        stack= []

        for i, v in enumerate(temperatures):
            # when stack is empty just add to the stack and continue since there's nothing to compare to
            if len(stack) == 0:
                stack.append((i,v))
                continue
            
            # grab top of stack and compare to current iteration to see if current temp is higher
            top = stack[-1]
            while v > top[1]:
                # if current iteration temp is higher then we subtract the indexes to get number of days and
                # set the top's corresponding index of our result array to the number of days
                res[top[0]] = i-top[0]
                stack.pop() #remove from stack since we found the result for that day
                # grab the new top to continue down the stack
                if len(stack) > 0:
                    top = stack[-1]
                else:
                    break
            # after comparing we should add current iteration to our stack
            stack.append((i,v))
        
        return res




