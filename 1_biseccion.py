import math

a = 0
b = 1
tol = pow(10, -2)
n = 3

def f (x):
    return math.sqrt(x) - math.cos(x)

def printMsg (i, a, b, p, f):
    msg = f"Resultado {i}\n"
    msg += f"\tValor de a: {a}\n"
    msg += f"\tValor de b: {b}\n"
    msg += f"\tValor de p: {p}\n"
    msg += f"\tValor de f(a): {f(a)}\n"
    msg += f"\tValor de f(b): {f(b)}\n"
    msg += f"\tValor de f(p): {f(p)}\n"
    msg += f"\tValor de f(b) x f(p): {f(a)*f(p)}\n"
    print(msg)

def bisection (a, b, tol, n):
    i = 1
    while (i <= n):
        p = a + ((b - a) / 2)
        m = (b - a) / 2
        
        if f(p) == 0 or m < tol:
            return f"Todo bien, el numero es {p}"
        printMsg(i, a, b, p, f)
        
        i += 1
        res = f(a) * f(p)
        if res > 0:
            a = p
        else:
            b = p
    return "Algo salio mal"

print(bisection(a, b, tol, n))
