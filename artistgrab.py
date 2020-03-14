import lyricsgenius


def remove_squares(test_str):
    ret = ''
    skip1c = 0
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif skip1c == 0:
            ret += i
    return ret


token = "YOUR TOKEN HERE"
genius = lyricsgenius.Genius(token)
f = open("artistlist.txt")
content = f.readlines()
f.close()
f = open("output.txt","w")
content = [x.strip() for x in content]
for artist in content:
    if artist == '' or artist is None:
        f.close()
        break
    result = genius.search_artist(artist, max_songs=20, sort="popularity")
    for song in result.songs:
        temp = song.lyrics
        temp = remove_squares(temp)
        temp = "".join([s for s in temp.splitlines(True) if s.strip("\r\n")])
        temp = temp + '\n' + "<|endoftext|>" + '\n'
        f.write(temp)
f.close()
