import sys, re
from collections import Counter

with open(sys.argv[1], 'r', encoding='utf-8') as file:
    words = re.findall(r'\w+', file.read())
    
contagem = Counter(words)
total_sum = sum(contagem.values())
c_sum = 0
print('_'*20)
for key, value in contagem.most_common(int(sys.argv[2])):
    print(f'{key}'.rjust(15), ' | ', f'{value}'.ljust(15))
    c_sum += value

print('_'*20)

print(
    f' There are {total_sum} words!\n',
    f'These {sys.argv[2]} most common words represents {c_sum / total_sum * 100:.1f}% of the content.',    
    )

try:
    print(f'The word {sys.argv[3]} occurs {contagem[sys.argv[3]]} times.')
except:
    None
    