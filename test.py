import random

def mulmod(a, b, mod):
    x = 0
    y = a % mod
    while b > 0:
        if b % 2 == 1:
            x = (x + y) % mod
        y = (y * 2) % mod
        b //= 2
    return x % mod

def modulo(base, exponent, mod):

    x = 1
    y = base
    while exponent > 0:
        if exponent % 2 == 1:
            x = (x * y) % mod
        y = (y * y) % mod
        exponent //= 2
    return x % mod

def miller(p, iteration):
    print(f"Miller-Rabin test for {p} with {iteration} iterations")
    if p < 2:
        print(f"p < 2, returning 0")
        return 0
    if p != 2 and p % 2 == 0:
        print(f"p is even but not 2, returning 0")
        return 0

    s = p - 1
    while s % 2 == 0:
        print(f"s = {s}, dividing by 2")
        s //= 2

    for i in range(iteration):
        a = random.randint(1, p - 1)
        print(f"Iteration {i + 1}: a = {a}")
        temp = s
        mod = modulo(a, temp, p)
        print(f"mod = {mod}")
        while temp != p - 1 and mod != 1 and mod != p - 1:
            mod = mulmod(mod, mod, p)
            temp *= 2
            print(f"  mod = {mod}, temp = {temp}")
        if mod != p - 1 and temp % 2 == 0:
            print(f"Computation failed, returning 0")
            return 0
    print(f"Computation succeeded, returning 1")
    return 1


def main():
    iteration = 5
    num = int(input("Enter integer to test primality: "))
    if miller(num, iteration):
        print(f"\n{num} is prime")
    else:
        print(f"\n{num} is not prime")

if __name__ == "__main__":
    main()

