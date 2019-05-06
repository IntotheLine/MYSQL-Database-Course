import re

phone_text = """
(748) 328-7711
(435) 604-5545
(234) 845-6547
(323) 887-987

#str.replace
print('With string replace:')
alt_phone_text = phone_text.replace('(', '', replace(') ', ''=.replace('-','')
print(alt_phone_text)

#re.sub
print('With re.sub:')
sub_phoe_text = re.sub(r'[^\d\n]', '', phone_text)
print(sub_phone_text)

