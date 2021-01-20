import re


def string_task(s):
    return re.sub(r'(\w)', r'.\1', re.sub(r'[aoeiuy]', '', s.lower()))


assert string_task("Tour") == ".t.r"
assert string_task("Codewars") == ".c.d.w.r.s"
assert string_task("aBAcAba") == ".b.c.b"
