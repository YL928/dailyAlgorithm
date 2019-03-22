def diStringMatch(S):
    """
    :type S: str
    :rtype: List[int]
    """
    from collections import deque

    table = deque(range(len(S)))
    res = []
    for s in S:
        if s=='I':
            res.append(table.popleft())
        else:
            res.append(table.pop())
    return res

print  diStringMatch("IDDI")
