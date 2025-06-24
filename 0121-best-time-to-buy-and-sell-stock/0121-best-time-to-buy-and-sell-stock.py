class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minSum = prices.copy()
        maxSum = prices.copy()
        for i in range(1, len(prices)):
            minSum[i] = min(minSum[i-1], prices[i])

        for j in range(len(prices)-2, -1, -1):
            maxSum[j] = max(maxSum[j+1], prices[j])

        max_p = 0
        print(minSum, maxSum)
        for i in range(len(prices)):
            max_p = max(max_p, maxSum[i]-minSum[i])
        return max_p

        # 711111
        # 766664
            

        # i = 0
        # j = len(prices)-1
        # max_p = 0
        # while i < j:
        #     max_p = max(max_p, prices[j]-prices[i])
        #     if prices[j]-prices[i+1] > prices[j-1] - prices[i]:
        #         i +=1
        #     else:
        #         j -=1
        # return max_p