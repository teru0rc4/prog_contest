def calc(N,X):
    if N%X ==0:
        return 3*N
    else:
        return 3*X*(int(N/X)) + calc(X,N-X*(int(N/X)))


N,X = list(map(int, input().split()))
X = min(X,N-X)
ans = calc(N-X,X)
print('%s' % str(ans))
