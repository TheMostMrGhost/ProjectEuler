import math

__all__=['leg_sym','modular_sqrt','inverse']

def leg_sym(a,p):
	ls=pow(a, (p - 1) // 2 ,p)
	if ls == p-1:
		return -1
	else:
		return ls



def modular_sqrt(a, p):

    def legendre_symbol(a, p):
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls

    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

def inverse(a,n):
	t=0
	nt=1
	r=n
	nr=a
	while nr != 0:
		q = r//nr
		r,nr = [nr,r - q * nr]
		t,nt = [nt,t - q * nt]
	if r > 1:
		return 0
	if t < 0:
		t=t+n
	return t
