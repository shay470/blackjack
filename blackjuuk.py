import random
import pandas as pd
import numpy as np
import time

wins = 0
losses = 0

def main():
    wins = 0
    losses = 0
    cards =[]
    ranks =['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits =['Hearts','Diamonds','Clubs','Spades',]

    player_hand = []
    dealer_hand = []
    end_game = True



    def make_a_card_deck():
        
        for rank in ranks:
            for suit in suits:
                a = rank
                b = suit
                if ranks.index(a) == 0:
                    c = 11
                elif ranks.index(a) > 9:
                    c = 10    
                else:
                    c = ranks.index(a) + 1

                new_card = (a,b,c)

                cards.append(new_card)

        
        return cards

    # make a card deck
    
    def score_hand(player_or_dealer):
            result = sum([x[2] for x in player_or_dealer])
            
            return result
    player_score = score_hand(player_hand)
    dealer_score = score_hand(dealer_hand)

    def give_player_card():
        player_hand.append(cards.pop(random.randint(0, len(cards)-1)))
        if player_score >= 22:
            if 'A' in player_hand:
                player_score - 10
            else:
                global end_game
                end_game = True
                losses += 1
                print('The player is Bust and has lost !!')
                show()
            
        elif player_score ==21:
            end_game = True
            wins += 1
            print('The player has won\n Blackjack for the player !!')
            show()
            
        return player_hand

    def give_dealer_card():
        dealer_hand.append(cards.pop(random.randint(0,len(cards)-1)))
        if dealer_score >=22:
            if 'A' in dealer_hand:
                dealer_score - 10
            else:
                global end_game
                end_game = True
                wins += 1
                print('The dealer is Bust \n  The player has won !!')
                show()
                
        elif dealer_score ==21:
            end_game = True
            losses += 1
            print('The player has lost \n Blackjuck for the Dealer !!')
            show()
        return dealer_hand


    def show_player_hand():
        print(f'this is the player hand   {player_hand} \n that is the total score: {score_hand(player_hand)}')


    def show():
        print(player_score,dealer_score )

    
    def action_of_player():
        act = input('what would you like to do ? Stand(S), Hit(H) ')# Double or Split )

        if act == 'H':
            
                give_player_card()
                show_player_hand()
                action_of_player()
                
        elif act == 'S':
            pass
        
        else:
            pass
        
        
    ############################################      
    make_a_card_deck()
    
    # give player two cards
    for _ in range(2):
        give_player_card()

    # give dealer two cards
    for _ in range(2):
        give_dealer_card()

    print(f'this is the dealer hand   {dealer_hand[1]}')

    while end_game == False:
        show_player_hand()
        action_of_player()

        print(f'this the hole card: {dealer_hand[0]} \n  the dealer hand is: {dealer_hand}')
            
        while score_hand(dealer_hand) <= 16:
            print('dealer takes another card')
            time.sleep(2)

            give_dealer_card()

        print('dealer is STAND ')


    if player_score > dealer_score:
        end_game = 1
        wins += 1
        print('The player has Won !!')
        show()
    else:
        end_game = 1
        losses += 1
        print('the player has lost')
        show()


    again = input('would you like play again ? \n Y for yes \n N for no')

    if again == 'Y':
        main()

    else:
        print('goodbye')
        time.sleep(2)
        exit

    return wins , losses
main()












        # if dealer_score >= 22:
        #     end_game = True
        #     wins += 1
        #     print('The player has Won !!')
        #     show()
















    # elif dealer_score >= 22:   # dealer
    #     if 'A' in dealer_hand:
    #         dealer_score - 10
            
        
    # if dealer_score == 21:
    #     # end_game = 1
    #     losses += 1
    #     print('The Dealer has Won!!')
    #     show()

    # elif player_score == 21 and dealer_score != 21:
    #     #end_game = 1
    #     wins += 1 
    #     print('The player has Won !!')
    #     show()
        

    # elif dealer_score >= 22:
    #     #end_game = 1
    #     wins += 1
    #     print('The player has Won !!')
    #     show()

    # elif player_score >= 22:
    #     #end_game = 1
    #     losses += 1
    #     print('the player has lost')
    #     show()

    # 
