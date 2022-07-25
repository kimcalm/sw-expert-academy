T = int(input())

for t in range(T):
    num_list = []
    
    N = int(input())
    tmp = N

    while True:
        trans_str = list(str(N))
        for letter in trans_str:
            num_list.append(letter)
        if len(set(num_list)) == 10:
            print(f'#{t+1} {N}' )
            break
        N += tmp

'''
5
1
2
11
1295
1692
'''