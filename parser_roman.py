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

def getValueFromRomanNum(romanValue):
    """
    Get decimal value from a roman value and handle error
    Input: Roman Value (i.e: I, V, X...)
    Output: Decimal value of roman value
    """
    value = romanDict.get(romanValue)
    if value:
        return value
    print("input string contained invalid numeral: %s",romanValue )
    exit()

def parseRomanString(romanValue):
    """
    Get total value from roman string
    Input: Roman String (i.e: LIV)
    Output: Value of the roman string
    """
    total = 0
    for index in range(len(romanValue) - 1):
        currentValue = getValueFromRomanNum(romanValue[index])
        nextValue = getValueFromRomanNum(romanValue[index + 1])

        if (currentValue < nextValue):
            total -= currentValue
            continue
        total += currentValue
    total += getValueFromRomanNum(romanValue[len(romanValue) - 1])
    return total

def toRomanString(queryString, symbols):
    """
    Get decimal value from a roman value and handle error
    Input: Roman Value (I, V, X...)
    Output: Decimal value of roman value
    """
    romanValue = ""
    for symbol in queryString.split(" "):
        romanValue += symbols.get(symbol)
    return romanValue