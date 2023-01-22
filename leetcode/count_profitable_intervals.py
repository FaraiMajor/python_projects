'''
 The stocks of a company are being surveyed to analyze the net profit of the company 
 over a period of several months. For an analysis parameter k, a group of k consecutive 
 months is said to be highly profitable if the values of the stock prices are strictly 
 increasing for those months. Given the stock prices of the company for n months and the
 analysis [parameter k, find the number os highly profitable intervals.
'''

# version 1


def count_profitable_intervals(prices, k):
    n = len(prices)
    count = 0
    for i in range(n-k+1):
        window = prices[i:i+k]
        if all(window[i] < window[i+1] for i in range(len(window)-1)):
            count += 1
    return count

# version 2


def count_profitable_intervals(prices, k):
    n = len(prices)
    count = 0
    for i in range(n-k+1):
        if all(prices[i] < prices[i+1] for i in range(i, i+k-1)):
            count += 1
    return count


# optimized version
def count_profitable_intervals(prices, k):
    count = 0
    streak = 1
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            streak += 1
            if streak == k:
                count += 1
                streak = 1
        else:
            streak = 1
    return count


stock = [1, 2, 3, 4]
k = 3
print(count_profitable_intervals(stock, k))
