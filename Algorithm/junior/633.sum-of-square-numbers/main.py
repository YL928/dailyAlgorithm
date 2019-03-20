# endcoding: utf-8
import math

# 暴力法
def judgeSquareSum(c):
    base = int(math.sqrt(c))
    if c == 1 + base* base:
        return True
    for i in range(base, 0, -1):
        m = math.sqrt(c - i*i)
        if m == int(m):
            return true
    return False
print judgeSquareSum(999999999)