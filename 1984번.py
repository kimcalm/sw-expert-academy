T = int(input())

for t in range(T):
    num_list = list(map(int, input().split()))

    num_list.pop(num_list.index(max(num_list)))
    num_list.pop(num_list.index(min(num_list)))

    avg = sum(num_list) / len(num_list)
    remainder = avg % 1 

    if remainder >= 0.5:
        avg = avg + 1 - remainder
    else:
        avg = avg - remainder

    print(f'#{t+1} {int(avg)}')


'''
3      
3 17 1 39 8 41 2 32 99 2 
22 8 5 123 7 2 63 7 3 46 
6 63 2 3 58 76 21 33 8 1 
'''