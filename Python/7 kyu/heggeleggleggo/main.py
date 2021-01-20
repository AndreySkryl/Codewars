import re


def heggeleggleggo(word):
    return re.sub(r'([bcdfghjklmnpqrstwyvxz])', r'\1egg', word, flags=re.IGNORECASE)


assert heggeleggleggo("hello") == "heggeleggleggo"
assert heggeleggleggo("code here") == "ceggodegge heggeregge"
assert heggeleggleggo("FUN KATA") == "FeggUNegg KeggATeggA"
assert heggeleggleggo("egg") == "egegggegg"
assert heggeleggleggo("Hello world") == "Heggeleggleggo weggoreggleggdegg"
assert heggeleggleggo("scrambled eggs") == "seggceggreggameggbeggleggedegg egegggeggsegg"
assert heggeleggleggo("eggy bread") == "egegggeggyegg beggreggeadegg"
