world_places = ['paris','colombo','barceylona','london']
#print the list in original order.
print("This is thge original list")
print(world_places)
#print the list in alphabetical order temporarily.
print("\nThis is temporarily sorted list in alphabetical order.")
print(sorted(world_places))

print("\nThis is thge original list again")
print(world_places)

#print the list in reverse alphabetical order temporarily.
print("\nThis is temporarily sorted list in reverse alphabetical order.")
print(sorted(world_places, reverse= True))

print("\nThis is thge original list again")
print(world_places)

#print the list in reverse order temporarily.
print("\nThis is temporarily sorted list in reverse order.")
world_places.reverse()
print(world_places)

#reverese the list order again
world_places.reverse()
print(world_places)

#sort the list in alphabetical order permanantly.
print("\nThis is permantly sorted list in alphabetical order.")
world_places.sort()
print(world_places)

#print the list in reverese alphabetical order.
world_places.sort(reverse=True)
print(world_places)

length_of_places =  len(world_places)
print(f"\nThe length of the list if {length_of_places}.")