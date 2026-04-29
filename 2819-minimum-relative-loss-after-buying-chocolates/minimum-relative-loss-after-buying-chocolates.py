class Solution:
    def minLoss(self, prices):
        price_with_index = [(price, i) for i, price in enumerate(prices)]
        price_with_index.sort()

        min_loss = float('inf')

        for i in range(1, len(price_with_index)):
            curr_price, curr_idx = price_with_index[i]
            prev_price, prev_idx = price_with_index[i-1]
            if curr_idx < prev_idx:
                loss = curr_price - prev_price
                min_loss = min(min_loss, loss)

        return min_loss
