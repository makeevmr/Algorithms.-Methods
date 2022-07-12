def memo(f):
    cache = {}

    def wrap(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return wrap


def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


fib = memo(fib)  # Теперь fib ссылается на функцию wrap, а f ссылается на fib | можно использовать @memo перед def fib
print(fib(80))
