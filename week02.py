scores = [100, 97, 88, 91]
hap = 0
count = 0

for score in scores:
    hap += score
    count += 1

average = hap / count
print(average)