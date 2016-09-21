from codecs import open
from constants import *
import string

def value_format(value):
    if value[0] in string.digits:
        return int(value)
    else:
        return value

def load_level_data(level_path):
    raw = None
    with open(level_path, 'r', 'utf-8') as f:
        raw = f.read()

    lines = raw.split('\n')
    line_no = 0
    data = []

    options = {}

    for i in range(line_no, len(lines)):
        line = lines[i].strip()
        if line.startswith('@'):
            key, value = line[1:].split('=',1)
            key = key.lower()
            if value.startswith('('):
                value = [value_format(x) for x in value[1:-1].split(',')]
            else:
                value = value_format(value)
            options[key] = value
        else:
            line_no = i
            break

    for i in range(line_no, len(lines)):
        line = lines[i].rstrip()
        length = len(line)
        if not length:
            continue
        j = 0
        line_data = []
        while j < length:
            char = line[j]
            if char in LOADER_SYMBOLS.keys():
                line_data.append(LOADER_SYMBOLS[char])
            elif char == ';':
                break
            else:
                raise Exception('Unexcept char "{}" at line {}:{}'.format(char, i+1, j+1))
            j += 1
        data.append(line_data)

    return {'data': data, 'options': options}
