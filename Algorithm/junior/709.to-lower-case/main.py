def toLowerCase(str):
    """
    :type str: str
    :rtype: str
    """
    res = ''
    for c in str:
        base = ord(c)
        if 64 < base < 91:
            res += chr(base + 32)
        else:
            res += c
    return res

print toLowerCase("Hello!s")