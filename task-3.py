import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    phone = re.sub(r'\D', '', phone_number)
    if phone.startswith('0'):
        return f"+38{phone}"
    if phone.startswith('38'):
        return f"+{phone}"
    else:
        return phone

normalized_numbers = [normalize_phone(num) for num in raw_numbers]
print(normalized_numbers)
