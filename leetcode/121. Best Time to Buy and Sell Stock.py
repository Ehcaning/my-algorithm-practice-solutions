import math


class Solution:
    def maxProfit(self, prices):
        cur_profit = 0
        lowest_purchase = math.inf

        for price in prices:
            cur_profit = max(cur_profit, price - lowest_purchase)
            lowest_purchase = min(lowest_purchase, price)

        return cur_profit


s = Solution()
assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert s.maxProfit([7, 6, 4, 3, 1]) == 0
