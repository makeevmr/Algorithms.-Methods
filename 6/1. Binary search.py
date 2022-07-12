def bin_search(lst, value):
    left = 0
    right = len(lst) - 1
    while left <= right:
        if lst[(left + right) // 2] == value:
            return (left + right) // 2 + 1
        elif lst[(left + right) // 2] > value:
            right = (left + right) // 2 - 1
        else:
            left = (left + right) // 2 + 1
    return -1


n, *A = map(int, input().split())
k, *B = map(int, input().split())
for i in range(k):
    print(bin_search(A, B[i]), end=' ')
