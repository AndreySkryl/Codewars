def reverse_words(s):
    return ' '.join(reversed(s.split()))


assert reverse_words("hello world!") == "world! hello"
