# import ticket

people = int(input("몇 명? "))
ages = list()
age = 0

for person in range(people):
    age = int(input("나이 ? "))
    ages.append(age)

print(ages)
