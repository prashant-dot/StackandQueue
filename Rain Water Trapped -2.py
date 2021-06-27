class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
        n=len(A)
        l,r=0,n-1
        lmx,rmx,ans=0,0,0
        while(l<r):
            if A[l]<=A[r]:
                water=lmx-A[l]
                if water>0:
                    ans+=water
                lmx=max(lmx,A[l])
                l+=1
            else:
                water=rmx-A[r]
                if water>0:
                    ans+=water
                rmx=max(rmx,A[r])
                r-=1
        return ans

==>TC=O(n) and SC=O(1)
