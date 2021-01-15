import re


def alphabet_war(battlefield):
    if '#' not in battlefield:
        matches = re.findall(r'\w+', battlefield)
        result = ''.join(matches)
        return result
    else:
        matches = re.findall(r'#|\[\w+\]', battlefield)
        items_and_hps = [[match, 2] if match != '#' else [match, 1] for match in matches]
        for i, item in enumerate(items_and_hps):
            if item[0] == '#':
                items_and_hps[i][1] = 0

                # left
                current_i = i - 1
                while 0 <= current_i:
                    if items_and_hps[current_i][0] != '#':
                        items_and_hps[current_i][1] -= 1
                        break
                    current_i -= 1
                # right
                current_i = i + 1
                while current_i < len(items_and_hps):
                    if items_and_hps[current_i][0] != '#':
                        items_and_hps[current_i][1] -= 1
                        break
                    current_i += 1
        alive_chars = list(filter(lambda item: item[1] > 0, items_and_hps))
        result = ''.join(list(map(lambda item: item[0][1:-1], alive_chars)))
        return result


assert alphabet_war('xm[u]gxc[dqch]p') == 'xmugxcdqchp'
assert alphabet_war('[a]asd#[b]#[c]') == 'ac'
assert alphabet_war('[a]#b#[c][d]') == 'd'
assert alphabet_war('[a][b][c]') == 'abc'
assert alphabet_war('##a[a]b[c]#') == 'c'
assert alphabet_war('abde[fgh]ijk') == 'abdefghijk'
assert alphabet_war('ab#de[fgh]ijk') == 'fgh'
assert alphabet_war('ab#de[fgh]ij#k') == ''
assert alphabet_war('##abde[fgh]ijk') == ''
assert alphabet_war('##abde[fgh]') == ''
assert alphabet_war('##abcde[fgh]') == ''
assert alphabet_war('abcde[fgh]') == 'abcdefgh'
assert alphabet_war('##abde[fgh]ijk[mn]op') == 'mn'
assert alphabet_war('#abde[fgh]i#jk[mn]op') == 'mn'
assert alphabet_war('[ab]adfd[dd]##[abe]dedf[ijk]d#d[h]#') == 'abijk'
