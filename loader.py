import string
import os
from codecs import open
from glob import glob

from constants import *
from level import Level

def ValuePaser(value):
    if value[0] in string.digits:
        return int(value)
    else:
        return value

def ListLevels():
    return sorted(glob("levels/*.lvl"))

def LoadLevel(level_path):
    raw = None

    if not level_path.startswith('levels'):
        level_path = os.path.join('levels', level_path)
    if not level_path.endswith('.lvl'):
        level_path += '.lvl'

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
                value = [ValuePaser(x) for x in value[1:-1].split(',')]
            else:
                value = ValuePaser(value)
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

    return Level(maze=data, **options)
