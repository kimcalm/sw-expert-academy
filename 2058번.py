num = int(input())

digit_sum = 0

while num > 0:
    remainder = num % 10
    num //= 10
    digit_sum += remainder

print(digit_sum)