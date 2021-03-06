# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/

def maxProfit(prices):
    profit = 0
    engaged = False
    current_stock_idx = 0
    for i,v in enumerate(prices):
        if engaged: # in a transaction
            # if more profit can be achieved, 
            # next stock more expensive
            try:
                if prices[i+1] >= v:
                    continue
                else:
                    profit += v - prices[current_stock_idx]
                    engaged = False
                    print('sell {} for {} profit'.format(prices[current_stock_idx], v-prices[current_stock_idx]))
            except:
                # reached end of list
                # check if there's profit to be made
                if prices[current_stock_idx] < v:
                    profit += v - prices[current_stock_idx]
                    print('sell {} for {} profit'.format(prices[current_stock_idx], v-prices[current_stock_idx]))
                    engaged = False
                break
        else: # if not engaged in transaction
            try:
                # if profit can be made by next step, buy
                if prices[i+1] > v:
                    current_stock_idx = i
                    print('buy {}'.format(prices[i]))
                    engaged = True 
            except:
                # end of list
                continue
    return profit

if __name__ == '__main__':
    r = maxProfit([7,1,5,3,6,4])
    print('result: {}'.format(r))
    assert(r == 7)
