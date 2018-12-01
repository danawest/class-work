def make_album(artist, title, tracks = 0):
    """Returns a dictionary of information about the album."""
    album_dict = {'artist': artist.title(), 'title': title.title()}
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict