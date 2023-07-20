import re
import pyperclip

casaRegex = re.compile(r'cas(a|al|amento)')
mo = casaRegex.search(pyperclip.paste())
print(mo.group())