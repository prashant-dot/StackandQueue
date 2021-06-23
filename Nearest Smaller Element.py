from collections import deque
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        stack=deque()
        l=[]
        for i in range(len(A)):
            x=-1
            while(len(stack)!=0 and stack[-1]>=A[i]):
                stack.pop()
            if len(stack)!=0: x=stack[-1]
            l.append(x)
            stack.append(A[i])
        return l       
==>TC=O(n) and SC=O(n)
