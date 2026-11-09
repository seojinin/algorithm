import sys
from functools import cmp_to_key

input = sys.stdin.readline

# left가 앞이면 음수, 같으면 0, 뒤면 양수
def comp(left, right):
    # 1순위: 일의 자리 비교
    if left % 10 != right % 10:
        return -1 if left % 10 < right % 10 else 1
    # 2순위: 십의 자리 비교
    if left // 10 % 10 != right // 10 % 10:
        return -1 if left // 10 % 10 < right // 10 % 10 else 1
    # 3순위: 백의 자리 비교
    if left // 100 != right // 100:
        return -1 if left // 100 < right // 100 else 1
    return 0


n = int(input())
a = [int(input()) for _ in range(n)]

a.sort(key=cmp_to_key(comp))
print('\n'.join(map(str, a)))  # 일괄 출력
