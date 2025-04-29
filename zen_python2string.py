import sys
with open(sys.prefix + '\\Lib\\this.py', 'r') as f:
    script = f.read()
script = script.replace('print("".join([d.get(c, c) for c in s]))', 'zen = "".join([d.get(c, c) for c in s])')
exec(script)

phrases = zen.split('\n')
for i in range(len(phrases)):
    if i > 1:
        print('| '+f'Principle {i-1}'.center(17), '| '+phrases[i])
    elif i == 0:
        print(phrases[i]+'(edited)\n')
        
input()