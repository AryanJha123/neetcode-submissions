class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                buy = i
                sell = i
            elif prices[i] > prices[sell]:
                sell = i
            if buy < sell:
                profit = max(profit, prices[sell]-prices[buy])
        return profit