N = int(input())

n = 1

while n <= N :
    cnt = 0
    num = n
    while num != 0:
        one_digit = num % 10
        num = num // 10
        if one_digit != 0 and one_digit % 3 == 0:
            cnt += 1
    
    if cnt > 0:
        print('{}'.format('-'*cnt), end=' ')
    else :
        print('{}'.format(n), end=' ')

    n += 1
