class Solution:
    def isValid(self, s :str)->bool:
        #stack data structure：correct->pop out
        #hash map :determine if a closing parentheses matches the open one
        #empty->TRUE
        #O(n)
        stack = []
        closeToOpen = { ")" : "(" , "]" : "[" , "}" : "{" }

        for  c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                #add to stack
        return True if not stack else False
