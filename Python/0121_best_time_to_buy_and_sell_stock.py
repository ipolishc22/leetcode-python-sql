# 121. Best Time to Buy and Sell Stock
#
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)

            else:
                left = right
            right += 1

        return max_profit
    

    # Another solution
    #
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxProfit2(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)

        return maxP