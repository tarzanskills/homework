def Check_Vowels(string, vowels):
    final = [each for each in string if each in vowels]
    print(len(final))
    print(final)


string = "pythonloopsareawesome"
vowels = "AaEeIiOoUu"
Check_Vowels(string, vowels);