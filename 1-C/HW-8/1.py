class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx = 0
        for i in range(len(accounts)):
            summ = 0
            for j in range(len(accounts[i])):
                summ += accounts[i][j]
            if summ >+ maxx :
                maxx = summ
        return maxx