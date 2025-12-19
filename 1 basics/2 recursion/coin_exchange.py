# Exchange the amount of cash with given denominations
# -1 if impossible

cash = int(input())
n = int(input())
coins = list(map(int, input().split()))

cache = [None for _ in range(cash + 1)]

def exchange(cash):
    if cache[cash] is not None:
        return cache[cash]
    if cash < 0:
        return -1
    if cash in coins:
        cache[cash] = 1
        return 1
    results = [exchange(cash - coin) for coin in coins]
    if max(results) == -1:
        cache[cash] = -1
        return -1
    else:
        results = [x for x in results if x >=0]
        cache[cash] = min(results) + 1
        return min(results) + 1
    
print(exchange(cash))
