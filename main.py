from translator import Translator

with open('input.txt') as f:
    lines = f.readlines()

translator = Translator()
for line in lines:
    query = line.strip()
    translator.parseCommand(query)

for result in translator.results:
    if result[0] != 'error':
        print(f'{result[0]} is {result[1]}')
    else:
        print(result[1])
