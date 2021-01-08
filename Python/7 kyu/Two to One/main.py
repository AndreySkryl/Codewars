def longest(s1, s2):
    return ''.join(sorted(list(
        set(s1).union(set(s2))
    )))


assert longest("aretheyhere", "yestheyarehere") == "aehrsty"
assert longest("loopingisfunbutdangerous", "lessdangerousthancoding") == "abcdefghilnoprstu"
assert longest("inmanylanguages", "theresapairoffunctions") == "acefghilmnoprstuy"