T = int(input())

for t in range(T):
    N,M = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))

    max_sum = 0

    if N == M:
        for i in range(len(ai)):
            result = 0
            result += ai[i] * bj[i]
            max_sum += result

    elif N < M:
        for i in range(M - N + 1):
            result = 0
            for j in range(len(ai)):
                result += ai[j] * bj[i+j]
            if max_sum < result:
                max_sum = result
    
    else:
        for i in range(N - M + 1):
            result = 0
            for j in range(len(bj)):
                result += bj[j] * ai[i+j]
            if max_sum < result:
                max_sum = result

    print('#{} {}'.format(t+1, max_sum))