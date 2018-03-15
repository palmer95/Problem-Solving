def sum_of_mults_of_3_and_5():
    res = 0
    for i in range(1, 1000):
        if not i % 3 or not i % 5:
            res += i
    return res


def even_fib():
    pre2 = 0
    pre = 1
    cur = pre + pre2
    even_terms = 0
    while pre2 < 4000000:
        pre2 = pre
        pre = cur
        cur = pre + pre2
        if pre2 % 2 == 0:
            even_terms += pre2

    return cur, even_terms


def sieve_of_eratosthenes(n):
    primes = []
    for i in range(2, n+1):
        if i not in primes:
            print i
            for j in range(i*i, n+1, i):
                primes.append(j)

def largest_prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return max(factors)


if __name__ == '__main__':
    # print sum_of_mults_of_3_and_5()
    # print even_fib()
    # sieve_of_eratosthenes(10)
    print largest_prime_factors(600851475143)
