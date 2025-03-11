print("Modifying Elements in a List")
motocycles = ['honda','yamaha','suzuki']
print(motocycles)

#modyfying elemennts
motocycles[0] = 'ducati'
print(motocycles)
print("\n")

print("Adding Elements to a List")
#Appending elements to a list
#appned method add new item to the end of list
motocycles.append('ducati')
print(motocycles)
print('\n')

#create a new list using append method
motobikes = []
motobikes.append('honda')
motobikes.append('yamaha')
motobikes.append('suzuki')

print(motobikes)
print('\n')

print('Inserting Elements into a list')
#Inserting elements into a list using insert method().
#This method allow us to add items into a list at any position.
motocycles = ['honda','yamaha','suzuki']
motocycles.insert(0,'ducati')
print(motocycles)
print('\n')

#if you know the position of the removing item then we can use del statemnet 
print("Removing elements from a list")
motocycles = ['honda','yamaha','suzuki']
print(motocycles)
del motocycles [0]
print(motocycles)
print('\n')

print("Removing item using pop() method and pop() method remove last item in a list")
#pop() method allow you to access removed item later
motocycles = ['honda','yamaha','suzuki']
print(motocycles)

poped_motocycles = motocycles.pop()
print(motocycles)
print(poped_motocycles)
print('\n')

print("Giving index of the list item to pop() method  you can remove any item in a list")
#giving index of the list item to pop() method  you can remove any item in a list
motocycles = ['honda','yamaha','suzuki']
print(motocycles)
first_owned = motocycles.pop(0)
print(motocycles)
print(f'The first motocycle I owned was a {first_owned.title()}.')
print('\n')

print('Removing an item by value')
motocycles = ['honda','yamaha','suzuki','ducati']
print(motocycles)

motocycles.remove('ducati')
print(motocycles)

too_expensive = 'yamaha'
motocycles.remove(too_expensive)
print(motocycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')
