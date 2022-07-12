def fib_digit(n):
    lst = [0, 1]
    for i in range(2, n + 1):
        lst.append((lst[0] + lst[1]) % 10)
        del lst[0]
    return lst[-1]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()

