def find_all_divisors(n):
    li = []
    i = 1
    while i * i <= n:
        if n%i == 0:
            li.append(i)
            if (n//i != i):
                li.append(n//i)
        i += 1
    return li

def naive_is_prime(n):
    # 2 divisors, 1 and itself
    cnt = 0
    for i in range(1,n+1):
        if n%i == 0:
            cnt += 1
    if cnt == 2:
        return "yes"
    else:
        return "no"
    
def better_is_prime(n):
    # 2 divisors, 1 and itself
    cnt = 0
    i = 1
    while i * i <= n:
        if n%i == 0:
            cnt += 1
            if n//i != i:
                cnt += 1
        i += 1
    if cnt == 2:
        return True
    else:
        return False

def print_all_prime_factors(n):
    # naive
    # TC o(sqrt(n)*2*sqrt(n)). only factors are going for prime check. so its approximate
    i = 1
    li = []
    while i * i <= n:
        if n%i == 0:
            if better_is_prime(i):
                li.append(i)
            if n//i != i:
                if better_is_prime(n//i):
                    li.append(n//i)
        i += 1
    return li

def better_print_all_prime_factors(n):
    # (n * logn)
    i = 2 
    li = []
    while i <= n:
        if n%i == 0:
            while n%i == 0:
                n = n // i
            li.append(i)
        i = i + 1
    return li

def best_print_all_prime_factors(n):
    # tc: o(sqrt(n) * logn)
    i = 2 
    li = []
    while i * i <= n:
        if n%i == 0:
            while n%i == 0:
                n = n // i
            li.append(i)
        i = i + 1
    if n != 1:
        li.append(n)
    return li

# remember, if u are finding factors then stick to sqrt method

n = 780
print("find_all_divisors", find_all_divisors(n))
print("naive_is_prime", naive_is_prime(n))
print("better_is_prime", better_is_prime(n))
print("printAllFactors", print_all_prime_factors(n))
print("better_print_all_prime_factors", better_print_all_prime_factors(n))
print("best_print_all_prime_factors", best_print_all_prime_factors(n))