T = int(input())

for t in range(T):
    N = int(input())

    num_list = list(map(int, input().split()))
    num_list.sort()

    print(f'#{t+1}', end=' ')

    for idx in range(N):
        print(f'{num_list[idx]}', end=' ')
    print()


'''
1
5
1 4 7 8 0
'''