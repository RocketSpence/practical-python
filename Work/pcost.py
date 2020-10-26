# Exercise 1.27

import csv
import sys

def portfoliocost(filename):
    '''
    returns total
    '''

    total = 0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(f)
        for row in rows:
            try:
                totalShares = int(row[1])
                pricePerShare = float(row[2])
                total += (totalShares * pricePerShare)
            except ValueError:
                print('Bad row', row)

        return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfoliocost(filename)
print(cost)
