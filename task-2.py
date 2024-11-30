import random

def get_numbers_ticket(min, max, quantity):
    return random.sample(range(min, max + 1), quantity)

get_numbers_ticket(1, 49, 6)
