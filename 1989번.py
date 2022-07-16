T = int(input())

data = [input().strip() for i in range(T)]
n = 1

for word in data:
    is_palindrome = 1
    for j in range((len(word)-1)//2):
        if word[j] != word[len(word)-1-j]:
            is_palindrome = 0
            break
    print('#{} {}'.format(n, is_palindrome))
    n += 1