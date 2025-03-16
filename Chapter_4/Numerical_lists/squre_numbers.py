#make a squre numbers list
squres = []

for value in range(1,11):
    squre = value **2
    squres.append(squre)
    
print(squres)

squres = []

for value in range(1,11):
    squres.append(value **2)
    
print(squres)
print("\n")

#simple statics with a list of numbers
print(min(squres))
print(max(squres))
print(sum(squres))
print("\n")

#List comprehension
squres = [value**2 for value in range(1,11)]
print(squres)