T = int(input())

prime_factor = [2, 3, 5, 7, 11]

for t in range(T):
    N = int(input())

    exponent = []

    for prime_num in prime_factor:
        cnt = 0
        while N % prime_num == 0:
            cnt += 1
            N //= prime_num
        
        exponent.append(cnt)

    print(f'#{t+1}', end=' ')

    for num in exponent:
        print(f'{num}', end=' ')
    print()





'''
2  
6791400
1646400
'''