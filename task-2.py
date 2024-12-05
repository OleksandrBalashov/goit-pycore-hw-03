import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <=1000 and quantity <= (max - min):
        return random.sample(range(min, max + 1), quantity)
    else:       
        return 'Not valid values'

print(get_numbers_ticket(1, 40, 6))
