class RomanNumerals:

    numerals = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }

    reversedNumerals = dict([[v, k] for k, v in numerals.items()])


    @classmethod
    def toRoman( self, num:str ) -> str:
        '''Convert number in base 10 to Roman numeral'''
        num_length = len(num)
        output = []
        for n in range(num_length):
            power = num_length - n - 1
            n_numeral = self.numerals[10 ** power]
            d = int(num[n])
            if d <= 3:
                output.append(n_numeral * d)
            elif 4 <= d <= 5:
                output.append(n_numeral * (5 % d) + self.numerals[5 * 10 ** power])
            elif 6 <= d <= 8:
                output.append(self.numerals[5 * 10 ** power] + n_numeral * (d % 5))
            else:
                output.append(n_numeral + self.numerals[10 ** (power + 1)])
        
        return "".join(output)
    

    @classmethod
    def fromRoman( self, num:str ) -> int:
        '''Convert Roman numeral to number in base 10'''
        num_length = len(num)

        output = 0
        p1, p2 = 0, 1
        while p2 < num_length:
            nextNum, prevNum = self.reversedNumerals[num[p2]], self.reversedNumerals[num[p1]]
            if nextNum <= prevNum:
                output += prevNum
            else:
                output -= prevNum

            p1, p2 = p2, p2 + 1

        output += self.reversedNumerals[num[-1]]

        return output