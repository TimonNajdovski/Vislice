def je_prastevilo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    kandidat = 3
    while kandidat ** 2 <= n:
        if n % kandidat == 0:
            return False
        else:
            kandidat += 1
    return True

for i in range(200):
    if je_prastevilo(i):
        print(i)
