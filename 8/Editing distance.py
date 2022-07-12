def diff(a, b):
    if a != b:
        return 1
    else:
        return 0


def edit_dist_td(i, j):
    if D[i][j] == float('inf'):
        if i == 0:
            D[i][j] = j
        elif j == 0:
            D[i][j] = i
        else:
            ins = edit_dist_td(i, j - 1) + 1
            delete = edit_dist_td(i - 1, j) + 1
            sub = edit_dist_td(i - 1, j - 1) + diff(A_str[i - 1], B_str[j - 1])
            D[i][j] = min(ins, delete, sub)
    return D[i][j]


A_str = input()
B_str = input()
D = [[float('inf') for j in range(len(B_str) + 1)] for i in range(len(A_str) + 1)]
print(edit_dist_td(len(A_str), len(B_str)))
