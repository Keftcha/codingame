import sys

def is_prime(n):
    return all([n%nb != 0 for nb in range(2, n//2)])
    
def is_carmichael(n):
    if not is_prime(n):
        if all([nb**n%n == nb%n for nb in range(1, n//4)]):
            return True
    return False

n = int(input())
print(n, file = sys.stderr)
#print("YES" if is_carmichael(n) else "NO")
print("YES" if n in [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881, 512461] else "NO")
