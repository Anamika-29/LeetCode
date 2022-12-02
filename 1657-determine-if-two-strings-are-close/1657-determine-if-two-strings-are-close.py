class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1=list(word1)
        w2=list(word2)
        d1=defaultdict(lambda:0)
        d2=defaultdict(lambda:0)
        for a in w1:
            d1[a]+=1
        for a in w2:
            d2[a]+=1
        d1v=list(d1.values())
        d2v=list(d2.values())
        k1=list(d1.keys())
        k2=list(d2.keys())
        k1.sort()
        k2.sort()
        d1v.sort()
        d2v.sort()
        return d1v==d2v and k1==k2   