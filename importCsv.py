import csv

def writeCSV(n, a, b, p, f):
    with open('bisection.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['n', 'a', 'b', 'p', 'f(p)'])
        spamwriter.writerow([f'{n}', f'{a}', f'{b}', f'{p}', f'{f(p)}'])

# writeCSV()