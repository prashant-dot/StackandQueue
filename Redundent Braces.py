from collections import deque
class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        d=deque()
        for i in A:
            if i==')':
                count=0
                while (len(d)==0 or d[-1]!='('):
                    d.pop()
                    count+=1
                d.pop()
                if count<=1: return 1
            d.append(i)
        return 0
                    
==>O(n) where n is lenth of string
