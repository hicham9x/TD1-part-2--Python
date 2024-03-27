def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

list_1k = [i for i in range(2, 1000) if is_prime(i)]

print(list_1k)