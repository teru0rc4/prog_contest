N = int(input())
L = list(map(int, input().split()))
sort_L = sorted(L)
ans = 0
for i in range(N):
    ans = ans + sort_L[2*i]
print('%s' % str(ans))
