class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        prices.sort(reverse=True)

        price_first = prices.pop()
        price_second = prices.pop()

        if money - price_first - price_second < 0:
            return money
        else:
            return money - price_first - price_second
