# наибольшая невозрастающая подпоследовательность O(n * log(n))
def binary_search(left, right, value):
    while left < right:
        if right - left == 1:
            if d[left] < value:
                right = left
            elif value <= d[right]:
                left = right + 1
            else:
                left = right
        else:
            middle = (left + right) // 2
            if d[middle] == value:
                left = middle
            elif d[middle] > value:
                left = middle + 1
            else:
                right = middle
            return binary_search(left, right, value)
    return left


leng = 0
n = int(input())
A = list(map(int, input().split()))
d = [float('inf')]
pos = [0 for _i in range(n + 1)]
pos[0] = -1
prev = [0 for i in range(n)]
for _i in range(n):
    d.append(float('-inf'))
for i in range(n):
    j = binary_search(0, len(d) - 1, A[i])
    if d[j - 1] >= A[i] >= d[j]:
        d[j] = A[i]
        pos[j] = i
        prev[i] = pos[j - 1]
        leng = max(leng, j)
p = pos[leng]
answer = []
while p != -1:
    answer.append(p + 1)
    p = prev[p]
answer = answer[::-1]
print(len(answer))
for i in answer:
    print(i, end=' ')
