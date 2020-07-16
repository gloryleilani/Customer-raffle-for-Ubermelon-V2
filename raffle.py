
"""Randomly pick customer and print customer info"""


from random import choice
from customers import get_customers_from_file


def choose_customer(contestants):
    """Pick random customer from a list of contestants."""
    
    chosen_winner = choice(contestants)
    print(f"Tell {chosen_winner.name} at {chosen_winner.email} that they've won")


def run_raffle(): 
    """#runs other functions, main file"""
    
    contestants = get_customers_from_file("customers.txt")
    choose_customer(contestants)

    
if __name__ == "__main__": 
    run_raffle()




