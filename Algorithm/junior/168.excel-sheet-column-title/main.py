def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    if (n-1)/26 == 0:
        return chr( 65 + (n-1)%26)
    else:
        return convertToTitle((n-1)/26) + chr( 65 + (n-1)%26)
 

print convertToTitle(701)