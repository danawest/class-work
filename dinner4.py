guests = ['serena williams', 'michelle obama', 'ruth bader ginsberg', 'cher', 'eleanor roosevelt', 'kristen bell', 'roxane gay']
message = "I'm so sorry! I can only invite two of you!"
print(message)
uninvited = guests.pop(5)
print('A long time ago we used to be friends, ' + uninvited.title() + ".")
unwelcome = guests.pop(3)
print('Sorry ' + unwelcome.title() + ", you can't come either.")
unforgiving = guests.pop(-1)
print("You won't be coming, " + unforgiving.title() + ".")
undead = guests.pop(0)
print("Better luck next time, " + undead.title() + ".")
unrelenting = guests.pop(-1)
print("You're dead " + unrelenting.title() + ", you don't eat!")
print("You can still come " + guests[0].title() + ".")
print("So can you, " + guests[1].title() + ".")
del guests[1]
del guests[0]
print(guests)
