contries = ['Sri Lanka','United Kingdom','America','France','Spain']
print("This is the original List\n",contries )

#modify a list item
contries[4] = 'Italy'
print('\n New list after modyfing the last item\n',contries)

#add a new item to the end of the list
contries.append('Greece') 
print("\nItem added to end of the list\n",contries)


#add new item to middle of the list
contries.insert(3,'Spain')
print('\n Insert a new item to the moddle of the list\n',contries)

#delete an item permanatly
del contries[3]
print('\n New list after deletin an item permanatly\n', contries)

#delete an item end of the list
contries.pop()
print('\n New list after deleting an item from the end of the list\n', contries)

#deleting an item from the given position
del_item = contries.pop(3)
print('\n new list after deletin an item from the given position\n',contries)

#access the deleted item
print(f'\nDeleted item is {del_item}.')

#removing an item with given value
contries.remove('United Kingdom')
print('\n New Listv after removin an item with given value\n', contries)

#organizing list temporary in alphabetical order
print('\nTemporary sorted list in alphabetical order\n', sorted(contries))
print('\nTemporary sorted list in reverse alphabetical order  \n', sorted(contries,reverse=True))

#organizing list permantly in alphabetical order
contries.sort()
print('\npermanant sorted list in alphabetical order\n',contries)

#reverse order of the list
contries.reverse()
print('\npermanant sorted list in reverse alphabetical order\n',contries)

print("\nLength of the list is :",len(contries))
