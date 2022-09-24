from game.cards import Cards


class Player:
    """
    A person who plays the game.

    The player is responsible for starting and controlling the game.

    Attributes:
        card (int): The current card.
        score (int): The score of the player.
        is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self):
        """
        Constructs a new Player.

        Args:
            self (Player): an instance of Player.
        """
        self.card = Cards()
        self.score = 300
        self.is_playing = True
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Player): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_outputs()

    def get_inputs(self):
        """
        Ask the user to guess if the next card will be higher or lower than the first card.

        Args:
            self (Player): an instance of Player.
        """
        old_card = self.card.getNumber()
        print(f'The card is: {old_card}')

        guess = ""
        while guess.lower() != 'h' or guess.lower() != 'l':
            guess = input('Higher or lower? [h/l]: ')
            self.c2 = Cards() # New card object
            new_card = self.c2.getNumber()  

            if guess.lower() == 'h' or guess.lower() == 'l':
                self.compare_values(guess, old_card, new_card)
                break
        
    def compare_values(self, guess, old_card, new_card):
        """
        Compare the values of the cards. The player earns 100 points if they guessed correctly but loses 75 points if they guessed incorrectly.

        Args:
            self (Director): An instance of Player
            guess (string): A guess if it is greater or lower than the current card.
            old_card (int): Value of the old card
            new_card (int): Value of the new card
        """

        if guess.lower() == 'h' or guess.lower() == 'high' or guess.lower() == 'higher':
            if new_card > old_card:
                self.do_updates(100, new_card)

            elif new_card < old_card:
                self.do_updates(-75, new_card)

        elif guess.lower() == 'l' or guess.lower() == 'low' or guess.lower() == 'lower':
            if new_card < old_card:
                self.do_updates(100, new_card)
        
            elif new_card > old_card:
                self.do_updates(-75, new_card)

    def do_updates(self, points, new_card):
        """
        Updates the player's score.

        Args:
            self (Player): an instance of Player.
        """
        self.score += points

        if self.score <= 0:
            self.is_playing = False
        
        self.card.number = new_card
    
    def do_outputs(self):
        """
        Displays the new cards, the score, and asks the player if they want to continue playing.

        Args:
            self (Player): an instance of Player.
        """

        print(f'The card was: {self.card.number}')
        print(f'Your score is: {self.score}')
        
        if self.score <= 0:
            self.is_playing = False
        else:
            # Ask player to continue or not
            ask = ""
            while ask.lower() != 'n' or ask.lower() != 'y':
                ask = input('Play again? [y/n]: ')

                if ask.lower() == 'y' or ask.lower() == 'yes':
                    self.is_playing = True
                    print()
                    break
                elif ask.lower() == 'n' or ask.lower() == 'no':
                    self.is_playing = False
                    break
                else:
                    print("Invalid input")
                
                

   

            

    