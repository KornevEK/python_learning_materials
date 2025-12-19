import math

# break 2N points on a plane into pairs so the sum distance in pairs is miminal
# uses bit mask approach
# famous olympiad problem

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def min_distance(points):
    n = len(points) // 2
    dp = [float('inf')] * (1 << (2*n))
    dp[0] = 0
    for mask in range(1 << (2*n)):
        x = bin(mask).count('1')
        if x % 2 == 0:
            for i in range(2*n):
                if not (mask & (1 << i)):
                    for j in range(i+1, 2*n):
                        if not (mask & (1 << j)):
                            new_mask = mask | (1 << i) | (1 << j)
                            dp[new_mask] = min(dp[new_mask], dp[mask] + distance(points[i], points[j]))
    return dp[-1]

points = []
n = int(input())
for i in range(n):
    a = tuple(map(int, input().split()))
    points.append(a)
print(min_distance(points))
