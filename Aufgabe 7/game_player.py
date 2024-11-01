__author__ = "Chris"

class PLAYER:
    '''
    Player class
    '''
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.points = 0
        self.trumpf = False
        self.trumpf_color = None

    def get_name(self):
        '''
        Returns the name of the player
        output:
            - name: str
                    name of the player
        '''
        return self.name

    def is_bot(self):
        '''
        Returns if the player is a bot
        output:
            - is_bot: bool
                if the player is a bot
        '''
        return False

    def pop_card(self, card:int):
        '''
        Removes a card from the players cards
        input:
            - card: int
                index of the card
        '''
        return self.cards.pop(card)

    def get_cards(self):
        '''
        Returns the cards of the player
        output:
            - cards: list
                list of cards of the player
        '''
        return self.cards

    def add_points(self, points):
        '''
        Adds points to the player
        input:
            - points: int
                points to add
        '''
        self.points += points

    def get_points(self):
        '''
        Returns the points of the player
        output:
            - points: int
                points of the player
        '''
        return self.points

    def add_card(self, card):
        '''
        Adds a card to the players cards
        input:
            - card: dict
                card to add
        '''
        self.cards.append(card)

    def set_cards(self, cards):
        '''
        Sets the cards of the player
        input:
            - cards: list
                list of cards
        '''
        self.cards = cards

if __name__ == "__main__":

    import game
    
    player = PLAYER("Bot", 1, game.create_cards())
    print(player.get_cards())
    print(player.play_card())
    print(player.get_cards())
