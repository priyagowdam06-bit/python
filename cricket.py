fobj = open("sachin.txt", "r")

strike_rates = []

for line in fobj:
    columns = line.split()

    runs = int(columns[2])
    balls = int(columns[3])

    sr = (runs / balls) * 100
    strike_rates.append(sr)

import statistics

deviation = statistics.stdev(strike_rates)

print(deviation)

fobj.close()