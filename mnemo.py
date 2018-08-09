#!env /bin/python
# CC-BY-SA

import sys, re
#import os

#Table des Regex par digit
d = {   "0": "(c[ieéèê]|[szç])",
        "1": "[td]",
        "2": "(n|gn)",
        "3": "m",
        "4": "r",
        "5": "l",
        "6": "([sc]h|g[eéèêiî]|j)",
        "7": "[gckqx]",
        "8": "(ph|[fvw])",
        "9": "[bp]"
        }

# voyelles éventuelles en début de mot
x = "^[haàâeéèêëiîïoôöuùûy-]*"

# itération
for c in sys.argv[1]:
    if c in d:
        x += d[c] + "[haàâeéèêëiîïoôöuùûyi-]*"
    else:
        x += c

# c'est plus rapide avec egrep sous linux
#os.system('egrep "'+x+'$" ./dico.txt')

pattern = re.compile(x+'$')
for i, line in enumerate(open('dico.txt')):
    for match in re.finditer(pattern, line):
        print (match.group())

