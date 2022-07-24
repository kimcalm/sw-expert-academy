T = int(input())

grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(T):
    N, K = map(int, input().split())

    all_scores= []
    rate = [0.35, 0.45, 0.2]

    for _ in range(N):
        student_score = list(map(int, input().split()))
        all_scores.append(student_score)

    for idx, score_list in enumerate(all_scores):
        total_score = 0
        for i in range(3):
            total_score += all_scores[idx][i] * rate[i]
        
        all_scores[idx].append(total_score)
        
    rank = 1
    for j in range(N):
        if all_scores[K-1][3] < all_scores[j][3]:
            rank += 1

    up_per = (rank / N) * 10

    if up_per % 1 != 0:
        up_per = up_per + 1

    up_per = int(up_per)

    print(f'#{t+1} {grade_list[up_per - 1]}')


'''
1
10 2
87 59 88
99 94 78
94 86 86
99 100 99
69 76 70
76 89 96
98 95 96
74 69 60
98 84 67
85 84 91
'''