cars = ['bmw','audi','toyota','subaru']
print(cars)
#sort  cars list in alphabatical order.
#sort method chnage the order permanantly.
cars.sort()
print(cars)
print('\n')

#sort the cars list to reverse alphatical order.
cars.sort(reverse= True)
print(cars)
print('\n')

#sorting a list temporarily
cars = ['bmw','audi','toyota','subaru']

print("Here is the original list")
print(cars)

print('\nHere is the sorted list')
print(sorted(cars))

print("\nHere is the original list again")
print(cars)
print('\n')

#printing a list in reverse order
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

#finding the length of the cars list
print(len(cars))