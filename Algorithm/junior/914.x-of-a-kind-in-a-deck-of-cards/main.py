def hasGroupsSizeX(deck):
    """
    :type deck: List[int]
    :rtype: bool
    """
    if len(deck)<2:
        return False
    num = set(deck)
    res = [deck.count(x) for x in num]
    mi= min(res)
    if mi == 1:
        return False
    for c in res:
        if c%mi != 0:
            if c%mi == 1:
                return False
            print c, mi, c%mi, mi%(c%mi)
            if mi%(c%mi) !=0:
                return False
    return True


print hasGroupsSizeX([1,1,1,2,2,2,3,3])