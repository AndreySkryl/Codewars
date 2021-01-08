def spin_words(sentence):
    length = 5
    words = sentence.split()
    modified_words = []
    for word in words:
        x = ''.join(list(reversed(word))) if len(word) >= length else word
        modified_words.append(x)
    return ' '.join(modified_words)


assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
assert spin_words("This is a test") == "This is a test"
assert spin_words("This is another test") == "This is rehtona test"


# best practice #1
def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


# best practice #2
import re
def spin_words(sentence):
    # Your code goes here
    return re.sub(r"\w{5,}", lambda w: w.group(0)[::-1], sentence)
