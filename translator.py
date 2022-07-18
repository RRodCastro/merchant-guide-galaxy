import re
from helpers.parser_roman import parseRomanString

symbolRegex = "^([\w]+) is ([A-Z]{1,2})$"
metalRegex = "^([a-zA-z ]+)\ ([I|i]ron|[S|s]ilver|[G|g]old) is ([\d]+) [C|c]redits"
creditsRegex = "^(how much|how many Credits)\ is\ ([a-zA-z ]+)(\??)$"
metalsMatch = ['silver', 'gold', 'iron']

symbolUnitEnum = {'intergalaticUnit': 0, 'romanNum': 1}
metalEnum = {'intergalaticUnits': 0, 'metalName': 1, 'credits': 2}


class Translator():
    def __init__(self):
        self.symbols = {}
        self.metals = {}
        self.queries = []
        self.results = []

    def parseCommand(self, query):
        """
        Determinate which operation needs to be done by matching the query with a regex, update attributes of class
        """

        if re.search(symbolRegex, query):
            x = re.findall(symbolRegex, query)
            self.symbols[x[0][symbolUnitEnum['intergalaticUnit']]
                         ] = x[0][symbolUnitEnum['romanNum']]
        elif re.search(metalRegex, query):
            x = re.findall(metalRegex, query)
            self.metals[(x[0][metalEnum['metalName']]).lower()] = {
                'amount': parseRomanString(
                    self.toRomanString(x[0][metalEnum['intergalaticUnits']], self.symbols)), 'credits': int(x[0][metalEnum['credits']])}
        elif re.search(creditsRegex, query):
            x = re.findall(creditsRegex, query)
            self.results.append(
                self.calculateTransaction(x[0][1].strip().lower()))
        else:
            self.results.append(
                ['error', 'I have no idea what you are talking about'])

    def calculateTransaction(self, query):
        """
        Calculate the credits or amount on a given transaction
        Input: Query in the galaxyan language
        Output: List with original query and amount/credits on that given transaction
        """
        if len(list(filter(lambda _: _ in query, metalsMatch))) > 0:
            query = query.split(' ')
            metal = query.pop(-1)
            romanString = ''
            for symbol in query:
                romanString += self.symbols.get(symbol)
            romanValue = parseRomanString(romanString)
            metalComposition = self.metals.get(metal)
            if not metalComposition:
                return ['error', 'I have no idea what you are talking about']
            transactionAmount = (
                romanValue * metalComposition['credits'] / metalComposition['amount']) if metalComposition['amount'] > 0 else 0
            return [' '.join(query) + ' ' + (metal.capitalize()), int(transactionAmount)]
        else:
            romanString = ''
            for symbol in query.split(' '):
                romanString += self.symbols.get(symbol)
            return [query, parseRomanString(romanString)]

    def toRomanString(self, query, symbols):
        """
        Get decimal value from a roman value and handle error
        Input: Roman Value (I, V, X...)
        Output: Decimal value of roman value
        """
        romanValue = ""
        for symbol in query.split(" "):
            romanValue += symbols.get(symbol)
        return romanValue

    def setSymbol(self, symbol):
        self.symbols[symbol[symbolUnitEnum['intergalaticUnit']]] = symbol[symbolUnitEnum['romanNum']]
    def getResults(self):
        return self.results