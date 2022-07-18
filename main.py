import re

from parser_roman import parse

symbolRegex = "^([\w]+) is ([A-Z]{1,2})$"
with open('test.txt') as f:
    lines = f.readlines()

symbols = {}

for line in lines:
    query = line.strip()
    if re.search(symbolRegex, query):
        x = re.findall(symbolRegex, query)
        symbols[x[0][0]] = x[0][1]
print(symbols)

test = "tegj glob prok"
romanString = ""

for symbol in test.split(" "):
    romanString += symbols.get(symbol)
print(parse(romanString))