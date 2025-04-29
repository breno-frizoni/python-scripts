import sys, re

def count_versicle(match):
    versicles.append(match.group())
    if match.start() == 0:
        return ''
    return '%'

versicles = []

with open(sys.argv[1], 'r', encoding='utf-8') as content:
    text = re.sub(r'[0-9][0-9]|[0-9]', count_versicle, content.read())

text = text.split('%')

assert len(versicles) == len(text)

for i in range(len(versicles)):
    text[i] = text[i].replace('\n', ' ')
    text[i] = text[i].strip()
    versicles[i] += f' - {text[i]}'
del text
try:
    print(versicles[int(sys.argv[2])-1])
except:
    print(f'syntax: python {sys.argv[0]} [chapterfile.txt] [versicle_number]')
    print(f'Try a versicle from 1 to {len(versicles)}')

