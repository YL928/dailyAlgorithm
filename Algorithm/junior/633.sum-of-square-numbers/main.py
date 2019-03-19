# endcoding: utf-8
import math


def judgeSquareSum(c):
    if c<2:
        return False 


    base = int(math.sqrt(c))
    if c == 1 + base* base:
        return True
    for i in xrange(int(base)):
        
        