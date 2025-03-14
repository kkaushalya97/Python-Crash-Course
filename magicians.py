magicians = ['alice','david','carolina']
#create a for loop to access the elements in the magicians list

for magician in magicians:
    print(magician.title())
    
print('\n')
    
#print a messsage to each magician
for magician in magicians:
    print(f'{magician.title()},that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}\n")

#print a thank you message to all once the for loop is terminated.
print("Thank you, everyone.that was a great magic show!.")
