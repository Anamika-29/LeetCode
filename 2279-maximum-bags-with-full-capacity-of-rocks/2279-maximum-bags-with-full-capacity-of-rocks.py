class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        dif=[capacity[i]-rocks[i] for i in range(len(rocks))]
        dif.sort()
        ct=0
        for i in range(len(dif)):
            if additionalRocks==0:
                break
            if additionalRocks>=dif[i]:
                ct+=1
                additionalRocks-=dif[i]
            else:
                break
        return ct