class IntegerToRoman:
    def __init__(self, number):
        self.number = number

    def convert(self):
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        roman = ""

        for value, symbol in values:
            while self.number >= value:
                roman += symbol
                self.number -= value

        return roman


# Create object
number = int(input("Enter an integer (1-3999): "))

if 1 <= number <= 3999:
    obj = IntegerToRoman(number)
    print("Roman Numeral:", obj.convert())
else:
    print("Please enter a number between 1 and 3999.")