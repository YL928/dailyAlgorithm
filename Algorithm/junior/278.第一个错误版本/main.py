
def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    start=1
    end=n
    while(start<=end):
        mid=start+(end-start)/2
        if not isBadVersion(mid) & isBadVersion(mid+1):
            return mid+1
        if not isBadVersion(mid):
            left = mid
        if isBadVersion(mid):
            right = mid

def isBadVersion(n):
    if n >= 3:
        return True
    return False
if __name__ == "__main__":
    firstBadVersion(5)