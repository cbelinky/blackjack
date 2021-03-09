import unittest
import blackjack_final

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        # setUp test method allowing us to test other methods with fixed
        # attributes to eliminate randomness during testing.
        
        self.test_game = blackjack_final.Blackjack()
        
    def test_init(self):
        """testing to check if the variable are to empty list and 0."""
        self.assertEqual(self.user_hand, [])
        self.assertEqual(self.dealer_hand, [])
        self.assertEqual(self.user_total, 0)
        self.assertEqual(self.dealer_total, 0)
        
        
    def test_deal_deck(self):
        """check to see if the number is randomly popped or not."""
        self.assertTrue(self.random.shuffle(self.deck))
        
    def test_hand_total(self):
        """Testing to check if the variables are set accordingly. Also, checking 
        that user_total and dealer_total is not none."""
        self.assertEqual(self.user_total,0)
        self.assertAlmostEqual(self.dealer_total,0)
        self.assertIsNotNone(self.user_total)
        self.assertIsNotNone(self.dealer_total)
    
    def test_hit(self):
        """checking to see if extra card is added to the original 
        value of the hand"""
        #create user hand
        self.test_game.user_hand = [10,"A"]
        hand = len(self.test_game.user_hand)
        #test initial length is correct
        self.assertTrue(hand == 2)
        #check to see that a card was added to user hand
        self.test_game.hit('user')
        hand = len(self.test_game.user_hand)
        self.assertTrue(hand == 3)
        #create dealer hand
        self.test_game.dealer_hand = [10,"A"]
        hand = len(self.test_game.dealer_hand)
        #test initial length is correct
        self.assertTrue(hand == 2)
        #check to see that a card was added to dealer hand
        self.test_game.hit('dealer')
        hand = len(self.test_game.dealer_hand)
        self.assertTrue(hand == 3)
        
    def test_show_hands(self):
        """checking to see if total value for dealer and user's hands is shown """
        self.assertEqual(self.user_total)
        self.assertAlmostEqual(self.dealer_total)
        self.assertIsNotNone(self.user_total)
        self.assertIsNotNone(self.dealer_total)
        
    def test_check_blackjack(self):
        """checking to see if dealer or user got a total value of 21"""
        #assign a hand to user would get a total of 21.
        self.test_game.user_hand = [10,"A"]
        self.test_game.dealer_hand = [5, 7, "K"]
        check = self.test_game.check_blackjack()
        self.assertTrue(check == 'user')
        #assign a hand to dealer would get a total of 21.
        self.test_game.user_hand = [10, "K"]
        self.test_game.dealer_hand = [5, 6, "J"]
        check2 = self.test_game.check_blackjack()
        self.assertTrue(check2 == 'dealer')
        #assign a hand to dealer and user where both would not get a total of 21.
        self.test_game.user_hand = ["Q", "K"]
        self.test_game.dealer_hand = [5, 7, "A"]
        check3 = self.test_game.check_blackjack()
        self.assertTrue(check3 == None)
    
    def test_check_bust(self):
        '''
        For both player and dealer hands, check that both hands are properly
        marked as bust when total is over 21, and that hand is properly not
        marked as a bust when hand is valid.
        '''
        #assign a hand to both dealer and player where dealer would bust.
        self.test_game.user_hand = [10,"J"]
        self.test_game.dealer_hand = [5, 7, "K"]
        #check that dealer busts
        bust_dealer = self.test_game.check_bust("dealer")
        self.assertTrue(bust_dealer == 1)
        #check that player does not bust
        bust_player = self.test_game.check_bust("player")
        self.assertTrue(bust_player == 2)
        #assign a hand to both dealer and player where player would bust.
        self.test_game.dealer_hand = [10, "J"]
        self.test_game.user_hand = [5, 7, "K"]
        #check that player busts
        bust = self.test_game.check_bust("player")
        self.assertTrue(bust == 0)
        #check that dealer does not bust
        bust_dealer = self.test_game.check_bust("dealer")
        self.assertTrue(bust_dealer == 2)
        
    def test_check_winner(self):
        '''
        check that correct hand is declared winner
        '''
        #player wins with blackjack case
        self.test_game.user_hand = [10, 8, 3] #21
        self.test_game.dealer_hand = [10, 2] #12
        player_wins_bj = self.test_game.check_winner()
        self.assertTrue(player_wins_bj == 0)
        #dealer wins with blackjack case
        self.test_game.dealer_hand = [10, 8, 3] #21
        self.test_game.user_hand = [10, 2] #12
        dealer_wins_bj = self.test_game.check_winner()
        self.assertTrue(dealer_wins_bj == 1)
        #player wins case
        self.test_game.user_hand = [10, 8, 2] #20
        self.test_game.dealer_hand = [10, 2] #12
        player_wins = self.test_game.check_winner()
        self.assertTrue(player_wins == 2)
        #dealer wins case
        self.test_game.dealer_hand = [10, 8, 2] #20
        self.test_game.user_hand = [10, 2] #12
        dealer_wins = self.test_game.check_winner()
        self.assertTrue(dealer_wins == 3)
        #draw case
        self.test_game.user_hand = [10, 8, 3] #21
        self.test_game.dealer_hand = [10, 8, 3] #21
        draw = self.test_game.check_winner()
        self.assertTrue(draw == 4)
            
