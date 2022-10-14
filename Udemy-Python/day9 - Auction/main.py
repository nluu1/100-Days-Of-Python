from replit import clear

from art import logo
print(logo)
#############
print("Welcome to the Secret Auction Program")
bidder_info = {}
bidding_finish = False
while not bidding_finish:

    name = input("What is your name?\n")
    bid = int(input("What's your bid?\n$ "))
    answer = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    bidder_info[name] = bid
    # print(bidder_info)
    
    if answer == 'no':
        bidding_finish = True
    elif answer == 'yes':
        clear()

def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner of this auction is {winner} with the highest bid amount of ${highest_bid}.")

highest_bidder(bidder_info)