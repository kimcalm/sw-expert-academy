T= int(input())

num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(T):
    
    data = list(map(int, input().split()))
    month_diff = data[2] - data[0]

    total_dates = sum(num_of_days[data[0]-1:data[0]-1 + month_diff]) + data[3] + 1 - data[1]

    print(f'#{t+1} {total_dates}')


'''
3 
3 1 3 31
5 5 8 15
7 17 12 24  
'''