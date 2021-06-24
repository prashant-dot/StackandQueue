from collections import deque
class Solution:
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):
        r=deque()
        l=deque()
        R,L=[],[]
        for i in range(len(A)):
            x=-1
            while(l and l[-1][0]>=A[i]): l.pop()
            if l : x=l[-1][1]
            L.append(x)
            l.append([A[i],i])
        for i in range(len(A)-1,-1,-1):
            x=len(A)
            while(r and r[-1][0]>=A[i]): r.pop()
            if r : x=r[-1][1]
            R.append(x)
            r.append([A[i],i])
        ans=float('-inf')
        for i in range(len(A)):
            L[i]+=1
            R[i]-=1
            ans=max(ans,A[i]*(R[i]-L[i]+1))
        return ans
==>TC = O(n) and SC = O(n)
class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        
        i, n = 0, len(A)
        
        max_area, stack = 0, []
        while i < n :
            if not stack or A[stack[-1]] <= A[i] :
                stack.append(i)
                i += 1
            else :
                top = stack.pop()
                
                area = (A[top])*(i - stack[-1] - 1 if stack else i)

                max_area = max(max_area, area)
            
        while stack :
            top = stack.pop()
                
            area = (A[top])*(i - stack[-1] - 1 if stack else i)

            max_area = max(max_area, area)
        
        return max_area
