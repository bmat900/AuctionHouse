check = True
question = ""
auction_dictionary = {}
print('Welcome to the auction house program!')


# Devolve o maior valor da subasta e o nome do ganhador em um dictionary.
def max_bid(dictionary):
    max = 0
    win = ''
    for i in dictionary:
        if dictionary[i] >= max:
            max = dictionary[i]
            win = i
    return max, win

#Input do programa
while check == True:
    a = input("What's your name: ")
    b = int(input("What's your bid? $"))
    auction_dictionary[a] = b
    question = input("Are there any other bidders? Type 'yes' or 'no'.")
    if question == 'no':
        check = False

winner_bid = max_bid(auction_dictionary)
participants = len(auction_dictionary)

print(f'With the participation of {participants} participants, the winner is {winner_bid[1]} with the bid of {winner_bid[0]}$!')
