# наибольшая последовательнократная подпоследовательность
def lisbottomup(lst):
    d = [0 for i in range(len(lst))]
    for i in range(0, len(lst)):
        d[i] = 1
        for j in range(0, i):
            if A[j] <= A[i] and A[i] % A[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = 0
    for i in range(0, len(lst)):
        ans = max(ans, d[i])
    return ans


n = int(input())
A = list(map(int, input().split()))
print(lisbottomup(A))
