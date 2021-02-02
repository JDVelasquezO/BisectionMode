import csv
import math

a = -2
b = -1
tol = pow(10, -2)
n = 8
dataIterations = []
p_ant = 0

def f (x):
    return (x**4) - 2*(x**3) - 4*(x**2) + 4*x + 4

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
        spamwriter.writerow(['n', 'a', 'b', 'p', 'f(a)', 'f(b)', 
            'f(p)', 'f(a)*f(p)', 'error'])
        
        for d in datas:
            spamwriter.writerow([d["i"], d["a"], d["b"], d["p"], d["fa"],
                d["fb"], d["fp"], d["fap"], d["err"]])

def fillDict(i, a, b, p, f, dataIteration):
    global p_ant
    dataIteration["i"] = i
    dataIteration["a"] = a
    dataIteration["b"] = b
    dataIteration["p"] = p
    dataIteration["fa"] = f(a)
    dataIteration["fb"] = f(b)
    dataIteration["fp"] = f(p)
    dataIteration["fap"] = f(a) * f(p)
    dataIteration["err"] = abs(p - p_ant)
    dataIterations.append(dataIteration)
    p_ant = p

def bisection (a, b, tol, n):
    i = 1
    while (i <= n):
        dataIteration = {}
        p = a + ((b - a) / 2)
        m = (b - a) / 2
        
        if f(p) == 0 or m < tol:
            writeCSV(dataIterations)
            return 0
        
        fillDict(i, a, b, p, f, dataIteration)
        
        i += 1
        res = f(a) * f(p)
        if res > 0:
            a = p
        else:
            b = p
    writeCSV(dataIterations)
    return 1

print(bisection(a, b, tol, n))
