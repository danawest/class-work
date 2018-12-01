guests = ['michelle obama', 'ruth bader ginsberg', 'toni morrison', 'kristen bell']
message = "Dear " + guests[0].title() + "," + "\nPlease join me for dinner on Saturday evening."
print(message)
print(" ")
message = "Dear " + guests[1].title() + "," + "\nI really hope you can join " + guests[0].title() + " and me."
print(message)
print(" ")
message = "Dear " + guests[2].title() + "," + "\nI really hope you can join " + guests[0].title() + ", " + guests[1].title() + " and me."
print(message)
print(" ")
message = "Dear " + guests[3].title() + "," + "\nI know how much you admire " + guests[0].title() + ", " + guests[1].title() + " and " + guests[2].title() + ", so I really hope you'll come."
print(message)