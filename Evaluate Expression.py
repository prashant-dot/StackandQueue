from collections import deque
class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
        d=deque()
        result=0
        dic = { "+": (lambda a, b: a + b),
          "-": (lambda a, b: a - b),
          "*": (lambda a, b: a * b),
          "/": (lambda a, b: a / b)
            }
        for i in A:
            if i not in dic:
                d.append(int(i))
            else:
                a=d.pop()
                b=d.pop()

                result=dic[i](b,a)
                d.append(int(result))
        return d.pop()



==>O(n) where n is size of string
