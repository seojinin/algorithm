import sys
input = sys.stdin.readline

# 우선순위 비교 (1순위 일의 자리, 2순위 십의 자리, 3순위 백의 자리)
def priority(x):
    return (x % 10, x // 10 % 10, x // 100)

n = int(input())
a = [int(input()) for _ in range(n)]

a.sort(key=priority)  # 튜플 앞 원소부터 비교
print('\n'.join(map(str, a)))  # 일괄 출력
