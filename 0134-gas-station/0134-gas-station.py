class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        candidate, debit, credit = None, 0, 0

        for i in range(len(gas)):
            credit += gas[i] - cost[i]
            if credit < 0:
                candidate, debit, credit = None, debit - credit, 0
            elif candidate is None: 
                candidate = i

        return candidate if credit >= debit else -1