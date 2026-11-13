import art
print(art.logo)

bids = {}

continue_bidding = True
while continue_bidding:
    bid_name = input("What is your name?")
    bid_amount = int(input("What is your bid?"))

    bids[bid_name] = bid_amount

    bid_again = input("Are there any bidders? Type 'y' for yes or 'n' for no.")

    if bid_again != 'y':
        continue_bidding = False
    else:
        print("\n" * 50)

winner_name = ""
max_bid = 0

for name in bids:
    if bids[name] > max_bid or max_bid == 0:
        winner_name = name
        max_bid = bids[name]

print(f"The winner is {winner_name} with a bid of ${max_bid}")