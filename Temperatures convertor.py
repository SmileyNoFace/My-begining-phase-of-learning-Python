temp = int(input("Temperature: "))
unit = input("C or F or K or R or Re ")

if unit.upper() == "C":
    converted1 = 9 / 5 * temp + 32
    converted2 = temp + 273.15
    converted3 = (temp + 273.15) * 9 / 5
    converted4 = temp * 4 / 5
    print(f"""The temperatures in Fahrenheit is {converted1} °F.
The temperatures in Kelvin is {converted2} K.
The temperatures in Rankine is {converted3} °Ra.
The temperatures in Réaumur is {converted4} °Re. """)
elif unit.upper() == "F":
    converted1 = 5 / 9 * (temp - 32)
    converted2 = 5 / 9 * (temp - 32) + 273
    converted3 = temp + 459.67
    converted4 = (temp - 32) * 4 / 9
    print(f"""The temperatures in Celsius is {converted1} °C.
The temperatures in Kelvin is {converted2} K.
The temperatures in Rankine is {converted3} °R.
The temperatures in Rèaumur is {converted4} °Re. """)
elif unit.upper() == "K":
    converted1 = temp - 273.15
    converted2 = 9 / 5 * (temp - 273.15) + 32
    converted3 = temp * 9 / 5
    converted4 = (temp - 273.15) * 4 / 5
    print(f"""The temperatures in Celsius is {converted1} °C.
The temperatures in Fahrenheit is {converted2} °F.
The temperatures in Rankine is {converted3} °R.
The temperatures in Rèaumur is {converted4} °Re. """)
elif unit.upper() == "R":
    converted1 = (temp - 491.67) * 5 / 9
    converted2 = temp - 459.67
    converted3 = temp * 5 / 9
    converted4 = (temp - 291.67) * 4 / 9
    print(f"""The temperatures in Celsius is {converted1} °C.
The temperatures in Fahrenheit is {converted2} °F.
The temperatures in Kelvin is {converted3} K.
The temperatures in Rèaumur is {converted4} °Re. """)
elif unit.upper() == "RE":
    converted1 = temp * 5 / 4
    converted2 = temp * 9 / 4 + 273.15
    converted3 = temp * 5 / 4 + 273.15
    converted4 = temp * 9 / 4 + 491.67
    print(f"""The temperatures in Celsius is {converted1} °C.
The temperatures in Fahrenheit is { converted2} °F.
The temperatures in Kelvin is {converted3} K.
The temperatures in Rakine is {converted4} °R. """)
else:
    print("Please enter the following letters as shown. ")
