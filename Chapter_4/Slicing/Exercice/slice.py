names = ['kasuni','james','charlie','sawani','geogina']
#print first three numbers
for name in names[0:3]:
    print("Hello",name.title())
    
print("this is my first three items in the list")

#make a slice from first three items
print(f'\n {names[0:3]}.\n')

#print thre names from the middle
for name in names[2:5]:
    print("Hello",name.title())

#make a slice from the middle of the list
print("\n",names[2:5],'\n')

#print last three items
for name in names[-3:]:
    print("last three iteams are:",name.title())
    
#slice of last three items
print("\n",names[-3:])