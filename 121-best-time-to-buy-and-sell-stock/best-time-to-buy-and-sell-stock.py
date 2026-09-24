class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        least_cp=prices[0]
        profit=0
        for price in prices:
            if price<least_cp:
                least_cp=price
            if price-least_cp>profit:
                profit=price-least_cp
        return profit
        
        