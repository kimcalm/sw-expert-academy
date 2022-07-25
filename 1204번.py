T = int(input())

for _ in range(T):
    N = int(input())
    scores_list = list(map(int, input().split()))
    sort_scores_list = list(set(scores_list))

    cnt_list = []

    for num in sort_scores_list:
        cnt = 0
        for score in scores_list:
            if num == score:
                cnt += 1

        cnt_list.append(cnt)

    max_value = sort_scores_list[cnt_list.index(max(cnt_list))]
    print(f'#{N} {max_value}')
