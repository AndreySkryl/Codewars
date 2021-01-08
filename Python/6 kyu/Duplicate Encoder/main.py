from collections import Counter


def duplicate_encode(word):
    ignore_case_word = word.lower()
    char_counts = Counter(ignore_case_word)
    return ''.join(['(' if char_counts[char] == 1 else ')' for char in ignore_case_word])


assert duplicate_encode("din") == '((('
assert duplicate_encode("recede") == '()()()'
assert duplicate_encode("Success") == ')())())'
assert duplicate_encode("(( @") == '))(('
