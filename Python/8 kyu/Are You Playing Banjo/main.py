def are_you_playing_banjo(name):
    return name + (" plays banjo" if name[0].lower() == 'r' else " does not play banjo")


assert are_you_playing_banjo("martin") == "martin does not play banjo"
assert are_you_playing_banjo("Rikke") == "Rikke plays banjo"
