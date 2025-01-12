def make_album(artist, title, tracks = None):
    """Build a dictionary containing information about an album."""
    album_dictionary = {'artist': artist.title(), 'title': title.title()}
    if tracks:
        album_dictionary['tracks']= tracks
    return album_dictionary

while True:
    print("\nGive a name of artist:")
    print('\nGive title of album.')
    print("\nGive number of tracks")
    print("\nWrite end to quit the program")
    
    artist = input('Name: ')
    if artist == 'end':
        break
    title = input('title: ')
    if title == 'end':
        break
    tracks = input('Number: ')
    if tracks == 'end':
        break
    
    album = make_album(artist, title, tracks)
    print(album)    