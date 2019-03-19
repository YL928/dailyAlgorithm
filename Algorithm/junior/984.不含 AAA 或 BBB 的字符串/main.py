# encoding: utf-8

#天秀解法，copy 
class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        a,b = 'a','b'
        if A>B:
            a,b = b,a
            A,B = B,A
        if 2*A>B:
            return (b+b+a)*(B-A)+(b+a)*(2*A-B)
        else:
            return (b+b+a)*A+b*(B-2*A)

# 暴力解法
