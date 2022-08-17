bids = {}
bidding_finished = False
def highest_bidder(bids_record):
    highest_amount = 0
    highest_bidder = ''
    for i in bids:
        # print(bids_record[i])
        if bids_record[i] > highest_amount:
            highest_amount = bids_record[i]
            highest_bidder = i
    print(f'Highest bidder is {highest_bidder}')
    print(f'Amount: ${highest_amount}')
while not bidding_finished:
    name = input('Type the name of bidder:\n')
    price = int(input('How much is your bid?\n$'))
    bids[name] = price
    should_continue = input('Is there a next bidder? Type y or n:\n')
    if should_continue == 'n':
        bidding_finished = True
        highest_bidder(bids)
print(bids)