T = int(input())

for t in range(T):
    time_datas = list(map(int, input().split()))

    hour = 0
    min = 0
    
    for idx, data in enumerate(time_datas):
        if idx % 2 == 0:
            hour += data
        else:
            min += data

    if min >= 60:
        min -= 60
        hour += 1
    
    if hour > 12:
        hour -= 12

    print(f'#{t+1} {hour} {min}')


'''
3 
3 17 1 39
8 22 5 10
6 53 2 12   
'''