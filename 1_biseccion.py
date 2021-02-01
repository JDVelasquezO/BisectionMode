import csv
import math

a = 0
b = 1
tol = pow(10, -2)
n = 3
dataIterations = []

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

def writeCSV(datas):
    with open('bisection.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['n', 'a', 'b', 'p', 'f(p)'])
        for d in datas:
            spamwriter.writerow([d["i"], d["a"], d["b"], d["p"], d["f"]])

def fillDict(i, a, b, p, f, dataIteration):
    dataIteration["i"] = i
    dataIteration["a"] = a
    dataIteration["b"] = b
    dataIteration["p"] = p
    dataIteration["f"] = f(p)
    dataIterations.append(dataIteration)

def bisection (a, b, tol, n):
    i = 1
    while (i <= n):
        dataIteration = {}
        p = a + ((b - a) / 2)
        m = (b - a) / 2
        
        if f(p) == 0 or m < tol:
            writeCSV(dataIteration)
            return f"Todo bien, el numero es {p}"
        
        fillDict(i, a, b, p, f, dataIteration)
        
        i += 1
        res = f(a) * f(p)
        if res > 0:
            a = p
        else:
            b = p
    writeCSV(dataIterations)
    return "No se llego al resultado"

print(bisection(a, b, tol, n))
