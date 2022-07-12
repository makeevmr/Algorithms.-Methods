n = int(input())
A = list(map(int, input().split()))


def count_sort(lst):
    new_a = [0 for _i in range(len(A))]
    b = [0 for _i in range(1, 11)]
    for i in range(len(lst)):
        b[A[i] - 1] += 1
    for i in range(1, 10):
        b[i] += b[i - 1]
    for i in range(n - 1, -1, -1):
        new_a[b[A[i] - 1] - 1] = A[i]
        b[A[i] - 1] -= 1
    return new_a


for j in count_sort(A):
    print(j, end=' ')
