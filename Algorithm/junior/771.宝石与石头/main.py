# 暴力遍历
def numJewelsInStones1(J, S):
    count = 0
    for j in J:
        count += S.count(j)
    return count
    # return sum(S.count(i) for i in J) // 列式推倒
# print numJewelsInStones1('aA', "aAAabbbBBB")