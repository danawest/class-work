def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album from user input."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        } 
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

title_prompt = "\nWhat is one of your favorite albums? "
artist_prompt = "\nWho is it by? "

print("\nEnter 'quit' at any time to exit.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    artist = input(artist_prompt)
    if artist == 'quit':
        break
    album = make_album(artist, title)
    print(album)

print("\nThanks for your response!")