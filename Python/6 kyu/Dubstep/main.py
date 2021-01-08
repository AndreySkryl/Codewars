import re


def song_decoder(song):
    return re.sub(r'\s{2,}', ' ', re.sub(r'WUB', ' ', song)).strip()


print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))