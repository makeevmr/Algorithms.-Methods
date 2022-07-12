def backpack_without_reps_bu(weight, lst):
    d = [[0 for _j in range(len(lst) + 1)] for _i in range(weight + 1)]
    for i in range(1, len(lst) + 1):
        for w in range(1, weight + 1):
            d[w][i] = d[w][i - 1]
            if lst[i - 1] <= w:
                d[w][i] = max(d[w][i], d[w - lst[i - 1]][i - 1] + lst[i - 1])

    return d[W][n]


W, n = map(int, input().split())
bullion_weights_lst = list(map(int, input().split()))
print(backpack_without_reps_bu(W, bullion_weights_lst))
