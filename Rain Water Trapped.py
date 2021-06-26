class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
        n=len(A)
        l,r=[0]*n,[0]*n
        l[0]=A[0]
        for i in range(len(A)):
            l[i]=max(l[i-1],A[i])
        r[n-1]=A[n-1]
        for i in range(n-2,-1,-1):
            r[i]=max(r[i+1],A[i])
        ans=0
        for i in range(n):
            water=min(l[i],r[i])-A[i]
            if water>0:
                ans+=water
            else:
                ans+=0
        return ans

==>TC=O(n) and SC=(n)
