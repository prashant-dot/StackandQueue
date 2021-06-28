from collections import deque
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):
        d=deque()
        n=len(A)
        ans=[]
        for i in range(n):
            if d and d[0]==i-B: d.popleft()
            while(d and A[i]>A[d[-1]]): d.pop()
            d.append(i)
            if (i+1)>=B: ans.append(A[d[0]])

        return ans
==>TC=O(n) and SC=O(n)
