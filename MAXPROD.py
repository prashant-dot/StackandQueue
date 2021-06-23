class Solution:

    def _first_greater(self, A, prev=True):
        stack, ans = list(), [0] * len(A)

        it = range(len(A)) if prev else range(len(A)-1, -1, -1)

        for i in it:
            while stack and A[i] >= A[stack[-1]]:
                stack.pop()
            ans[i] = stack[-1] if stack else 0
            stack.append(i)
        return ans

    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        left = self._first_greater(A)
        right = self._first_greater(A, prev=False)
        maxx = -float('inf')

        for l, r in zip(left, right):
            maxx = max(l * r, maxx)

        return maxx % 1000000007
==> TC=O(n) and SC=O(n)       
      
from collections import deque
class Solution:
	# @param A : list of integers
	# @return an integer
	def maxSpecialProduct(self, A):
        left=deque()
        right=deque()
        l=[]
        r=[]
        for i in range(len(A)):
            x=0
            while(len(left)!=0 and left[-1][0]<=A[i]): left.pop()
            if len(left)!=0 : x=left[-1][1]
            l.append(x)
            left.append([A[i],i])
        for i in range(len(A)-1,-1,-1):
            x=0
            while(len(right)!=0 and right[-1][0]<=A[i]): right.pop()
            if len(right)!=0 : x=right[-1][1]
            r.append(x)
            right.append([A[i],i])
        maxx = -float('inf')

        for lr, rr in zip(l, r):
            maxx = max(lr * rr, maxx)

        return maxx % 1000000007
