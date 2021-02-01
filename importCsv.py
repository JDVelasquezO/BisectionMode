import csv

def writeCSV(a, b, p, f):
    with open('bisection.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['a', 'b', 'p', 'f(a)', 'f(b)', 'f(p)'])
        spamwriter.writerow([f'{a}', f'{b}', f'{p}', f'{f(a)}', f'{f(b)}', f'{f(p)}'])

# writeCSV()