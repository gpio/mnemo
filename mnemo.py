#!env /bin/python
# CC-BY-SA

import sys, os

#Table des Regex par digit
d = {   "0": "(ce|ci|[zsç])",
        "1": "[td]",
        "2": "(n|gn)",
        "3": "m",
        "4": "r",
        "5": "l",
        "6": "(ch|ge|gé|gè|gê|gi|j)",
        "7": "(ga|geu|go|gu|ca|co|cu|[kq])",
        "8": "(ph|[fv])",
        "9": "[bp]"
        }

# voyelles éventuelles en début de mot
x = "^[haàâeéèêëiïoôöuùûy]*"

# itération
for c in sys.argv[1]:
    if c in d:
        x += d[c] + "[aàâeéèêëiïoôöuùûy]*"
    else:
        x += c

# debug: affiche l'expression)
#print(x+"$")

# execution de grep avec le regex sur l'ensemble du dico
os.system('egrep "'+x+'$" ./dico.txt')
