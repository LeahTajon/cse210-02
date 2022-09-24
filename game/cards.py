import random

class Cards:
    """
    Each card have a number from 1 to 13.

    The value of the card is used for the main function of the game.

    Attributes:
        number (int): The number of the card drawn.
    """
    def __init__(self):
        """
        Constructs instances of Cards

        Args:
            self (card): an instance of a card.
        """
        self.number = random.randint(1, 13)
    
    def getNumber(self):
        """
        Returns the valus of the card.

        Args:
            self (card): an instance of a card.
        """

        return self.number





