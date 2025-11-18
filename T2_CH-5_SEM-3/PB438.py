N = int(input("Enter size of matrix (N): "))
A = []
print("Enter matrix elements row by row:")
for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)
for i in range(N):
    for j in range(i + 1, N):
        A[i][j], A[j][i] = A[j][i], A[i][j]
for i in range(N):
    A[i].reverse()
print("\nRotated Matrix (90° Clockwise):")
for row in A:
    print(*row)