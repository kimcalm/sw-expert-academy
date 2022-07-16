import math

N = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[math.ceil(len(data)/2)-1])