import unittest
from helpers.parser_roman import parseRomanString
from translator import Translator


class Test(unittest.TestCase):
    def testSmallRoman(self):
        """
        Test roman string to value (less than 100)
        """
        res = parseRomanString("LIV")
        self.assertEqual(res, 54)

    def testBigRoman(self):
        """
        Test roman string to value (greater than 1000)
        """
        res = parseRomanString("MCMIII")
        self.assertEqual(res, 1903)

    def testGetResults(self):
        """
        Test result get function
        """
        translator = Translator()
        res = translator.getResults()
        self.assertEqual(res, [])

    def testAmountResult(self):
        """
        Test amount with new symbol
        """
        translator = Translator()
        translator.setSymbol(['glob', 'I'])
        translator.setSymbol(['prok', 'V'])
        translator.setSymbol(['pish', 'X'])
        translator.setSymbol(['tegj', 'L'])
        translator.setSymbol(['jox', 'C'])

        translator.parseCommand("how much is jox pish jox glob pish ?")
        res = translator.getResults()
        self.assertEqual(res[0][1], 199)

    def testAmountCredits(self):
        """
        Test credits with new symbol
        """
        translator = Translator()
        translator.setSymbol(['glob', 'I'])
        translator.setSymbol(['prok', 'V'])
        translator.setSymbol(['pish', 'X'])
        translator.setSymbol(['tegj', 'L'])
        translator.setSymbol(['jox', 'C'])

        translator.parseCommand('glob glob Silver is 64 Credits')
        translator.parseCommand("how many Credits is pish glob glob Silver ?")
        res = translator.getResults()
        self.assertEqual(res[0][1], 384)
    
    def testError(self):
        """
        Test unkown command
        """
        translator = Translator()
        translator.setSymbol(['glob', 'I'])
        translator.setSymbol(['prok', 'V'])
        translator.setSymbol(['pish', 'X'])
        translator.setSymbol(['tegj', 'L'])
        translator.setSymbol(['jox', 'C'])

        translator.parseCommand("how many burgers I can get ?")
        res = translator.getResults()
        self.assertEqual(res[0][0], "error")

if __name__ == '__main__':
    unittest.main()
