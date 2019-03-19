
def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    left=1
    right=n
    if isBadVersion(1):
        return 1
    while(left<=right):
        mid=left+(right-left)/2
        mid_check = isBadVersion(mid)
        mid_1_check = isBadVersion(mid+1)
        if (not mid_check) & mid_1_check:
            return mid+1
        elif mid_check & mid_1_check:
            right = mid
        elif (not mid_check) & (not mid_1_check):
            left = mid
        

def isBadVersion(n):
    if n >= 5:
        return True
    return False
if __name__ == "__main__":
    print "first bed is :{}".format(firstBadVersion(5))