def make_album(artist,title):
    """Build dictionary that describing a music album"""
    album = {'artist': artist.title(), 'title': title.title()}
    return album

music_album = make_album('shadow','imperfect time')
print(music_album)

music_album = make_album('justin beiber', 'sorry')
print(music_album)

music_album = make_album('shwan', 'senorita')
print(music_album)

def make_album(artist,title, tracks=None):
    """Build dictionary that describing a music album"""
    album = {'artist': artist.title(), 'title': title.title()}
    if tracks:
        album['tracks'] = tracks
    return album

music_album = make_album('shadow', 'imperfect time')
print(music_album) 

music_album = make_album('larry', 'alone', tracks=7)
print(music_album)   

music_album = make_album('deck', 'check engine', tracks=9)
print(music_album)