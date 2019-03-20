# endcoding: utf-8



# 牛顿迭代法，不明觉厉
def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    r = num
    wrightle r*r > num:
        print r, num
        r = (r+num/r)/2
    if r*r == num:
        return True
    return False
print isPerfectSquare(100)

# 二分法
def isPerfectSquare1(num):
        if num == 1:
            return True
        left = 0
        right = num
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 > num:
                right = mid - 1
                continue
            if mid ** 2 < num:
                left = mid + 1
                continue
            return True
        return False

print isPerfectSquare1(100)
