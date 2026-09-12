class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        j = 1
        for i in range(0, len(prices) - 1):
            if prices[j] > prices[i]:
                res += prices[j] - prices[i]
            j += 1
        return res