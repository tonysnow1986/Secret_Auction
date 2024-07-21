from replit import clear
from Art import logo

print(logo)

bids = {}
finish_bidding = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        amount = bidding_record[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not finish_bidding:
    name = input("What ia your name?: ")
    price = int(input("How much is your bid?:  $"))
    bids[name] = price
    will_continue = input("Are there any other bidders remaining? Type yes or no ")
    if will_continue == "no":
        finish_bidding = True
        find_highest_bidder(bids)
    elif will_continue == "yes":
        clear()
