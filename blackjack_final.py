"""
A Blackjack Game Code.

This program will allow user to play blackjack game make a bet at the beginning 
of the game. This game will also allow users to ask for more cards if desire to
or stay put where they are. This game will create a hand for the dealer, and 
user will be playing with the dealer. This blackjack game is only one player 
game with dealer. 
"""

import random

class Blackjack:
    """ Creating a class named Blackjack, which have ability to read in players 
    bet, and set player hand. 
    """
     
    def __init__(self):
        """ Defining all of the attributes such as:deck, user hand, dealer hand,
        totaluser, and total dealer. First, assign all of cards value to the 
        deck variable setting deck, user hand, and dealer hand to empty list. 
        Setting total user and dealer to 0. 
        """
        self.deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]*4
        self.user_hand = []
        self.dealer_hand = []
        self.user_total = 0
        self.dealer_total = 0

    def deal_deck(self):
        """ In this function, randomly assign 4 cards to the user with 
        randomly popped number attached to the each card. cards are called card1,
        card2, card3, and card4. Function will not return anything, it will only 
        generate 4 random numbers and assign each number to the card1,2,3,4.  
        """
        random.shuffle(self.deck)
        card1 = self.deck.pop()
        self.user_hand.append(card1)
        card2 = self.deck.pop()
        self.dealer_hand.append(card2)
        card3 = self.deck.pop()
        self.user_hand.append(card3)
        card4 = self.deck.pop()
        self.dealer_hand.append(card4)

    def hand_total(self, hand_type):
        """ Setting / assigning the hands for the user and dealer with the number
        value. set K R J to 10 points, and A to 11 points.
        
        
        Args: hand_type:
        
        Returns: Total the number of points for the user and delear in user 
        and delear total. 
        
        """
        self.user_total = 0
        self.dealer_total = 0
        if hand_type == "user":
            for card in self.user_hand:
                if card == "J" or card == "Q" or card == "K":
                    self.user_total +=10
                elif card == "A":
                    if self.user_total >= 11:
                        self.user_total += 1
                    else:
                        self.user_total += 11
                else:
                    self.user_total += card
            return self.user_total
        elif hand_type == "dealer":
            for card in self.dealer_hand:
                if card == "J" or card == "Q" or card == "K":
                    self.dealer_total +=10
                elif card == "A":
                    if self.dealer_total >= 11:
                        self.dealer_total += 1
                    else:
                        self.dealer_total += 11
                else:
                    self.dealer_total += card
            return self.dealer_total

    def hit(self,hand_type):
        """ User/Dealer is asking to be a dealt another card. The value of the 
        card will be added to the total of fhe user or dealer.

        Arguments:
        hand_type {str} --a string that represents a user or the dealer's hand
        """
        random.shuffle(self.deck)
        card = self.deck.pop()
        if card == 11:
            card = "J"
        elif card == 12:
            card = "Q"
        elif card == 13:
            card = "K"
        elif card == 14:
            card = "A"
        if hand_type == "user":
            self.user_hand.append(card)
        elif hand_type == "dealer":
            self.dealer_hand.append(card)
            

    def show_hands(self):
        """Prints the user's and dealer's hand
       
        Returns:
        String -- representing the total value of the user's and dealer's hand.
         
        """
        print("Your hand was: "+ str(self.user_hand)[1:-1] + 
              " for a score of: "+ str(self.hand_total("user")))
        print("The dealer's hand was: "+ str(self.dealer_hand)[1:-1] + 
              " for a score of: "+ str(self.hand_total("dealer")))
    

    def check_blackjack(self):
        """Checks the total user's hand and dealer's hand to see if their 
        total is equal to 21.
    
        Returns:
        User -- The user's hand is equal to 21.
        Dealer -- The driver's hand is equal to 21.
        None - The driver's or user's hand is not equal to 21.
        """
        if self.hand_total("user") == 21:
            return "user"
        elif self.hand_total("dealer") == 21:
            return "dealer"
        else:
            return None
    
    def check_bust(self, hand_type):
        """ Prints the dealer's and user's hand to the console and compares the 
        score of each hand to determine if the the hand was a bust (score higher 
        than 21)
        Arguments:
        hand_type {str} -- a string that represents a user or the dealer's hand.
        Returns:
        0 {int} -- an int representing that the user has busted.
        1 {int} -- an int representing that the dealer has busted.
        2 {int} -- an int representing that there is no bust.
        """
        if hand_type == "user":
            if self.hand_total("user") > 21:
                return 0
            else:
                return 2
        elif hand_type == "dealer":
            if self.hand_total("dealer") > 21:
                return 1
            else:
                return 2

    def check_winner(self):
        """Checks the score of the player and dealer's cards and prints the 
        results to the user.
        Returns:
        0 {int} -- an int representing a user blackjack.
        1 {int} -- an int representing a dealer blackjack.
        2 {int} -- an int representing a user victory.
        3 {int} -- an int representing a dealer victory
        4 {int} -- an int representing a draw.
        """
        if self.hand_total("user") == 21:
            self.show_hands()
            return 0
        elif self.hand_total("dealer") == 21:
            self.show_hands()
            return 1
        elif self.hand_total("user") > self.hand_total("dealer"):
            self.show_hands()
            return 2
        elif self.hand_total("user") < self.hand_total("dealer"):
            self.show_hands()
            return 3
        elif self.hand_total("user") == self.hand_total("dealer"):
            self.show_hands()
            return 4

def play_game():
    """Driver function used to create a new blackjack game object and allow the
    user to play.
    """
    print("Let's play some Blackjack!")
    new_game = Blackjack()
    new_game.deal_deck()
    while True:
        print("The dealer's revealed card is: "+ str(new_game.dealer_hand[0]))
        print("Your hand is: "+ str(new_game.user_hand)[1:-1] +
              " for a total of: "+ str(new_game.hand_total("user")))
        if new_game.check_blackjack() == "user":
            print("Congrats you win with a Blackjack!")
            exit()
        elif new_game.check_blackjack() == "dealer":
            print("I'm sorry, the dealer got a Blackjack, you lose.")
            exit()
        elif new_game.check_blackjack == None:
            continue
        user_action = input("Do you want to Hit, Stand, or Exit?").lower()
        if user_action == "hit":
            new_game.hit("user")
            check_user_bust = new_game.check_bust("user")
            if check_user_bust == 0:
                print("Your hand was: "+ str(new_game.user_hand)[1:-1] +
                      " for a score of: "+ str(new_game.hand_total("user")))
                print("Sorry you busted. You lose.")
                exit()
        elif user_action == "stand":
            break
        elif user_action == "exit":
            exit()
        elif user_action != "hit" and user_action != "stand" and \
                                                user_action != "exit":
            raise ValueError
    while new_game.hand_total("dealer") < 17:
                new_game.hit("dealer")
                check_dealer_bust = new_game.check_bust("dealer")
                if check_dealer_bust == 1:
                    print("The dealer's hand was: "+ str(new_game.dealer_hand)
                          [1:-1] + " for a total of: " + 
                          str(new_game.hand_total("dealer")))
                    print("The dealer busted, you win!")
                    exit()
    winner = new_game.check_winner()
    if winner == 0:
        print("Congrats, you got a Blackjack!")
    elif winner == 1:
        print("I'm sorry, the dealer got a Blackjack, you lose.")
    elif winner == 2:
        print("Your hand score is greater then the dealer, you win!")
    elif winner == 3:
        print("The dealer's hand score is greater then yours, you lose.")
    elif winner == 4:
        print("The dealer's hand score is equal to yours, it's a draw.")
        

if __name__ == "__main__":
    play_game()