#slicing a list
players = ['charls','martina','michael','florence','eli']
#print 1 to 3 elements
print(players[0:3])

#print 2 to 4th elements
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#for loop in a slice
print("\nHere are the first three players in my team.")
for player in players[0:3]:
    print(player.title())