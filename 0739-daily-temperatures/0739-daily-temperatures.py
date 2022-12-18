class Solution:
    def dailyTemperatures(self, T):
    #initialize the result array with all '0's considering when there is no bigger temperature
        ans = [0]*len(T) 
        stack = []

        for i,v in enumerate(T):
            #check whether current val is greater than the last appended stack value.  We will pop all the elements which is lesser than the current temp
            while stack and stack[-1][1] < v:
                index,value = stack.pop()
                ans[index] = i - index # we are checking how many indices we have crossed since we last have a lesser temperature
            #Remember since we are comparing all the stack elements before inserting,all the stack elements will have temperatures greater than the current value	
            stack.append([i,v])      

        return ans   