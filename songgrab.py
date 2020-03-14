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
f = open("songlist.txt")
content = f.readlines()
f.close()
f = open("test_output.txt","w")
content = [x.strip() for x in content]
for song in content:
    if song == '' or song is None:
        continue
    if song[0] == '#':
        artist = song[1:]
    else:
        result = genius.search_song(song, artist)
        temp = result.lyrics
        temp = remove_squares(temp)
        temp = "".join([s for s in temp.splitlines(True) if s.strip("\r\n")])
        temp = temp + '\n' + "<|endoftext|>" + '\n'
        f.write(temp)

f.close()
