import re

phone_text = """
(749) 328-7711
null
(888) 333-2390
(232) 323-223
not anumber
+44 7070123456
"""

phone_numbers = ['(749) 328-7711', 'null', '(888) 333-2390', '+44 7070123456', '(761) 870-4352']

#good for smaller text, to search for the start of a text/pattern
print('Match:')
for ph in phone_numbers:
if re.match('\(\d{3}\)', ph): 
print(ph)

### search is good to searcha complete string
print()
print('Search:')
res = re.search('\(761\) 870-4352', phone_text
span = res.span()
print(span)
print(phone_text[span[0}:span[1]])
