def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    tep = []
    for word in words:
        work_mos = ''
        for c in word:
            work_mos += table[ord(c)-97]
        tep.append(work_mos)
    return len(set(tep))

print uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])