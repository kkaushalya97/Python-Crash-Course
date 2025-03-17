my_pizza = ['magerita','peperoni','chicken']
friend_pizza = my_pizza[:]

#add new item to original list
my_pizza.append('salame')
#add new item to friend list
friend_pizza.append('beef')

print(my_pizza)
print(friend_pizza)

#print list items are in a for loop
print("\nMy favorite pizza are:")
for pizza in my_pizza:
    print(pizza.title())
    
#print friends favorite pizza
print("\nMy friend's favorite pizza are:")
for value in friend_pizza:
    print(value.title())
