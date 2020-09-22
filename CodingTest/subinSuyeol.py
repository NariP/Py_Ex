# N, B = input(), list(map(int, input().split()))

N = 4
B = [3, 2, 3, 5]
A = [0 for i in range(N)]
A[0] = B[0]

for i in range(1, N):
    A[i] = (B[i]*(i+1) - sum(A))

for i in A:
    print(i, end = ' ')

print(A)