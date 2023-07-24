def solution(m, musicinfo):
    length = len(musicinfo)
    musics, queue = [[]]*length, []
    sharp_pair = {'C#':'c', 'D#':'d', 'F#':'f', 'G#':'g', 'A#':'a'}.items()
    for sharp in sharp_pair:
        m = m.replace(sharp[0], sharp[1])
    for i in range(length):
        musics[i] = musicinfo[i].split(',')
        for j in range(2):
            musics[i][j] = list(map(int, musics[i][j].split(':')))
            musics[i][j] = musics[i][j][0]*60 + musics[i][j][1]
        musics[i][1] -= musics[i][0]
        for sharp in sharp_pair:
            musics[i][3] = musics[i][3].replace(sharp[0], sharp[1])
        melody = divmod(musics[i][1], len(musics[i][3]))
        musics[i][3] = musics[i][3]*melody[0] + musics[i][3][0:melody[1]]
        
    for music in musics:
        if m in music[3]:
            queue.append(music)
    if queue:
        queue.sort(key=lambda x:x[1], reverse=True)
        return queue[0][2]
    else:
        return '(None)'