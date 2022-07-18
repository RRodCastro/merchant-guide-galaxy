from sys import exit

romanDict = {
  'M': 1000,
  'D': 500,
  'C': 100,
  'L': 50,
  'X': 10,
  'V': 5,
  'I': 1
}

def getValue(romanValue):
    value = romanDict.get(romanValue)
    if value:
        return value
    print("input string contained invalid numeral: %s",romanValue )
    exit()

def parse(romanString):
    sum = 0
    for index in range(len(romanString) - 1):
        currentValue = getValue(romanString[index])
        nextValue = getValue(romanString[index + 1])

        if (currentValue < nextValue):
            sum -= currentValue
            continue
        sum += currentValue
    sum += getValue(romanString[len(romanString) - 1])
    return sum
