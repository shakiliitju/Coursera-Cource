# Uses python3
def calc_fib(n):
    f = [0, 1]
    for i in range(2, n + 1):
        num_new = f[i - 1] + f[i - 2]
        f.append(num_new)
    return f[n]
n = int(input())
print(calc_fib(n))