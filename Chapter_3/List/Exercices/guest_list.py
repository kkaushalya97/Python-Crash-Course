guests = ['kasuni','james','sawani','georgina','charlie']
print(f'Hello {guests[0].title()} I would like to invite you for dinner.')
print(f'Hello {guests[1].title()} I would like to invite you for dinner.')
print(f'Hello {guests[2].title()} I would like to invite you for dinner.')
print(f'Hello {guests[3].title()} I would like to invite you for dinner.')
print(f'Hello {guests[4].title()} I would like to invite you for dinner.')
print('\n')

print(f'Hello All unfortunately {guests[2].title()} could not able to make it for dinner.')
print('\n')

#replace index two with value 'Kumari'
guests[2] = 'kumari'
print(guests)
print('\n')

print(f'Hello {guests[0].title()} I would like to invite you for dinner.')
print(f'Hello {guests[1].title()} I would like to invite you for dinner.')
print(f'Hello {guests[2].title()} I would like to invite you for dinner.')
print(f'Hello {guests[3].title()} I would like to invite you for dinner.')
print(f'Hello {guests[4].title()} I would like to invite you for dinner.')
print('\n')

print(f'Hello {guests[0].title()} I manage to find a bigger table for the dinner.')
print(f'Hello {guests[1].title()} I manage to find a bigger table for the dinner.')
print(f'Hello {guests[2].title()} I manage to find a bigger table for the dinner.')
print(f'Hello {guests[3].title()} I manage to find a bigger table for the dinner.')
print(f'Hello {guests[4].title()} I manage to find a bigger table for the dinner.')
print('\n')

#insert one new member to begining of the list
print(guests)
guests.insert(0,'antonella') 
print(guests)
#insert one new member to middle of the list
guests.insert(3,'taylor')
print(guests)
#add one new member to end of the list
guests.append('swift')
print(guests)
print('\n')

#invitation message to each member in the list
print(f'Hello {guests[0].title()} I would like to invite you for dinner.')
print(f'Hello {guests[1].title()} I would like to invite you for dinner.')
print(f'Hello {guests[2].title()} I would like to invite you for dinner.')
print(f'Hello {guests[3].title()} I would like to invite you for dinner.')
print(f'Hello {guests[4].title()} I would like to invite you for dinner.')
print(f'Hello {guests[5].title()} I would like to invite you for dinner.')
print(f'Hello {guests[6].title()} I would like to invite you for dinner.')
print(f'Hello {guests[7].title()} I would like to invite you for dinner.')
print('\n')

print(f'Hello {guests[0].title()} I would like to invite you for dinner.')
print(f'Hello {guests[1].title()} I would like to invite you for dinner.')
print(f'Hello {guests[2].title()} I would like to invite you for dinner.')
print(f'Hello {guests[3].title()} I would like to invite you for dinner.')
print(f'Hello {guests[4].title()} I would like to invite you for dinner.')
print(f'Hello {guests[5].title()} I would like to invite you for dinner.')
print(f'Hello {guests[6].title()} I would like to invite you for dinner.')
print(f'Hello {guests[7].title()} I would like to invite you for dinner.')
print('\n')

print(f'Hello {guests[0].title()} I am sorry I can only invite for two people for dinner due to table will not arrive on time.')
print(f'Hello {guests[1].title()} I am sorry I can only invite for two people for dinner due to table will not arrive on time.')
print(f'Hello {guests[2].title()} I am sorry I can only invite for two people for dinner due to table will not arrive on time.')
print(f'Hello {guests[3].title()} I am sorry I can only invite for two people for dinner due to table will not arrive on time.')
print(f'Hello {guests[4].title()} I am sorry I can only invite for two people for dinner due to table will not arrive on time.')
print(f'Hello {guests[5].title()} I am sorry I can only invite for two people for dinner due to table will not arrive on time.')
print(f'Hello {guests[6].title()} I am sorry I can only invite for two people for dinner due to table will not arrive on time.')
print(f'Hello {guests[7].title()} I am sorry I can only invite for two people for dinner due to table will not arrive on time.')
print('\n')

#removing items from the list and access the deleted iyem after removing from the list.
print("Removing Guests from the list")
print(guests)
removed_guest = guests.pop()
print(f'I am sorry {removed_guest.title()} I can not invite you for dinner.')
print('\n')

print(guests)
removed_guest = guests.pop()
print(f'I am sorry {removed_guest.title()} I can not invite you for dinner.')
print('\n')

print(guests)
removed_guest = guests.pop()
print(f'I am sorry {removed_guest.title()} I can not invite you for dinner.')
print('\n')

print(guests)
removed_guest = guests.pop()
print(f'I am sorry {removed_guest.title()} I can not invite you for dinner.')
print('\n')

print(guests)
removed_guest = guests.pop()
print(f'I am sorry {removed_guest.title()} I can not invite you for dinner.')
print('\n')

print(guests)
removed_guest = guests.pop()
print(f'I am sorry {removed_guest.title()} I can not invite you for dinner.')
print('\n')

print(guests)
print('\n')

print(f'Hi {guests[0].title()} you are still invited for the dinner.')
print(f'Hi {guests[1].title()} you are still invited for the dinner.')
print('\n')

#removing last two items from the list to make a empty list.
del guests[1]
print(guests)

del guests[0]
print(guests)


