from collections import deque
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        d=deque()
        for i in A:
            if i=="(":
                d.append("(")
            else:
                if len(d)==0:
                    return 0
                d.pop()
        if len(d)==0:
            return 1
        return 0
==>O(n) where n is lenth of string
