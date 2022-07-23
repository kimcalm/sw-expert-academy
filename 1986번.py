T = int(input())

for t in range(T):
    total = 0
    
    N = int(input())
    for i in range(1, N+1):
        if i % 2 != 1:
            i = -i
        total += i
    
    print(f'#{t+1} {total}')




'''
2
5
6
'''