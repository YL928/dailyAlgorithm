def repeatedNTimes(A):
    """
    :type A: List[int]
    :rtype: int
    """
    for a in set(A):
        if A.count(a)>1:
            return a
print repeatedNTimes([1,2,3,3])