guests = ['michelle obama', 'ruth bader ginsberg', 'eleanor roosevelt', 'kristen bell']
message = ("Good news! I found a larger table!")
print(message)
guests.insert(0, 'serena williams')
guests.insert(3, 'cher')
guests.append('roxane gay')
print(guests)
message = "Dear " + guests[0].title() + "," + "\nPlease come to my dinner party!"
print(message)
message = "Dear " + guests[1].title() + "," + "\nPlease come to my dinner party!"
print(message)
message = "Dear " + guests[2].title() + "," + "\nPlease come to my dinner party!"
print(message)
message = "Dear " + guests[3].title() + "," + "\nPlease come to my dinner party!"
print(message)
message = "Dear " + guests[4].title() + "," + "\nPlease come to my dinner party!"
print(message)
message = "Dear " + guests[-2].title() + "," + "\nPlease come to my dinner party!"
print(message)
message = "Dear " + guests[-1].title() + "," + "\nPlease come to my dinner party!"
print(message)