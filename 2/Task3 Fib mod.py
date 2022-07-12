def fib_mod(n, m):
    lst = [0, 1]
    find = False
    for i in range(2, n + 1):
        if (lst[i - 2] + lst[i - 1]) % m == 0 and ((lst[i - 2] + lst[i - 1]) % m + lst[i - 1]) % m == 1:
            find = True
            break
        else:
            lst.append((lst[i - 2] + lst[i - 1]) % m)
    if find:
        return lst[(n % len(lst))]
    return lst[-1]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
