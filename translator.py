import re
from parser_roman import parseRomanString

symbolRegex = "^([\w]+) is ([A-Z]{1,2})$"
metalRegex = "^([a-zA-z ]+)\ ([I|i]ron|[S|s]ilver|[G|g]old) is ([\d]+) [C|c]redits"
creditsRegex = "^(how much|how many Credits)\ is\ ([a-zA-z ]+)(\??)$"
metalsMatch = ["silver", "gold", "iron"]


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
            self.symbols[x[0][0]] = x[0][1]
        elif re.search(metalRegex, query):
            x = re.findall(metalRegex, query)
            self.metals[(x[0][1]).lower()] = {"amount": parseRomanString(
                self.toRomanString(x[0][0], self.symbols)), "credits": int(x[0][2])}
        elif re.search(creditsRegex, query):
            x = re.findall(creditsRegex, query)
            self.results.append(self.calculateTransaction(x[0][1].strip().lower()))
        else:
            self.results.append(["error" , "I have no idea what you are talking about"])

    def calculateTransaction(self, query):
        """
        Calculate the credits or amount on a given transaction
        Input: Query in the galaxyan language
        Output: List with original query and amount/credits on that given transaction
        """
        if len(list(filter(lambda _: _ in query, metalsMatch))) > 0:
            query = query.split(" ")
            metal = query.pop(-1)
            romanString = ""
            for symbol in query:
                romanString += self.symbols.get(symbol)
            romanValue = parseRomanString(romanString)
            metalComposition = self.metals[metal]
            transactionAmount = (
                romanValue * metalComposition["credits"] / metalComposition["amount"]) if metalComposition["amount"] > 0 else 0
            return [" ".join(query) + " " + (metal.capitalize()), int(transactionAmount)]
        else:
            romanString = ""
            for symbol in query.split(" "):
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
