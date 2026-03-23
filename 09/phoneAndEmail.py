import re

import pyperclip

# Create phone number regex
phone_re = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))?              # Area code - 123 ou (123) - optionnel (le ? à la fin)
    (\s|-|\.)?                      # Separator - un ' ' ou un '-' ou un '.' optionnel (le ?)
    (\d{3})                         # First three digits
    (\s|-|\.)                       # Separator - un ' ' ou un '-' ou un '.'
    (\d{4})                         # Last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))? # Extension - des espaces suivi de ext, x ou ext. (optionnel)
    )""",
    re.VERBOSE,
)

# Create email regex
email_re = re.compile(
    r"""(
    [a-zA-Z0-9._%+-]+   # Username (nombres, caractères. min ou MAJ, . _ + % -)
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # Domain name (nombres, caractères . min ou MAJ, . -)
    (\.[a-zA-Z]{2,4})   # Dot-something caractères . min ou MAJ
    )""",
    re.VERBOSE,
)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phone_re.findall(text):
    # groups[1] = area code, groups[3] = first 3 digits, groups[5] = last 4
    phone_num = "-".join([groups[1], groups[3], groups[5]])
    # groups[8] est l'indice correct pour le numéro d'extension (\d{2,5})
    if groups[8] != "":
        phone_num += " x" + groups[8]
    matches.append(phone_num)
for groups in email_re.findall(text):
    # On ne veut que le premier élément du tuple (l'email complet)
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard:")
    print("\n".join(matches))
else:
    print("No phone numbers or email adresses found.")
