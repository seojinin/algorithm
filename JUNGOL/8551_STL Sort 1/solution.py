import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x,y = map(int, input().split())

a[x:y+1] = sorted(a[x:y+1])
print(*a)

a.sort()
print(*a)
