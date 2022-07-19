T = int(input())

for t in range(T):
    sentence = input()
    lst =  [sentence[0]]

    for i in range(1, len(sentence)):
        if sentence[i] != sentence[0]:
            lst.append(sentence[i])
        else:
            is_same = 1
            for j in range(1, i):
                if sentence[i+j] != sentence[j]:
                    is_same = 0
                    break
            
            if is_same == 0:
                lst.append(sentence[i])
            else:
                break

    print(f'#{t+1} {len(lst)}')





'''
3       
KOREAKOREAKOREAKOREAKOREAKOREA
SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
GALAXYGALAXYGALAXYGALAXYGALAXY     
'''