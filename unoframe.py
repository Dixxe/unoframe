from random import randint, random

class Uno():

    _POSSIBLE_COLORS = ['red', 'green', 'blue', 'black']
    _POSSIBLE_ABILITIES = ['reverse', 'skip_move', '+2', '+4-field-color-change', 'field-color-change']
    # Uno._way is how game plays: counter clockwise or clockwise.
    # True - clockwise; False - counter clockwise.  
    # Uno._players is dictionary to manipulate card abilities and
    # card dispencing. 
    # {player_id : [player_card, player_card2]}.  

    def __init__(self, start_card, way: bool, cards_amount: int, players: dict):
        self._card_on_field = start_card # Card. 
        self._way = way 
        self._cards_amount = cards_amount 
        self._players = players
        self._move = 1 # Amount of moves during the game
        self._move_constant = 1 # For changing game's way. 

        self.player_on_demand = str

    def lay_card(self, card, player):
        if (card.number == self._card_on_field.number) or (card.color == self._card_on_field.color) or (card.color == "black"):
            self._card_on_field = card
            card_index = self._players[player].index(card)
            self._players[player].pop(card_index)

            self._move += self._move_constant
            try:self.handle_abilities(card)
            except Exception: pass
            self.player_on_demand = list(self._players.keys())[self._move % len(self._players)]
            return True
        else:
            self.give_card(1, self.player_on_demand)
            return False

    def handle_abilities(self, card):
        next_player = list(self._players.keys())[(self._move) % len(self._players)]

        if card.ability == 'reverse':
            if(self._move_constant == 1): self._move_constant = -1
            else: self._move_constant = 1
            self._move += 1 * self._move_constant
        elif card.ability == 'skip_move':
            self._move += 1 * self._move_constant
        elif card.ability == '+2':
            self.give_card(2, next_player)
        elif card.ability == '+4-field-color-change':
            self.give_card(4, next_player)

    def change_way(self):
        if (self._way == True): self._way = False
        else: self._way = True

    # Color is index of _POSSIBLE_COLORS. 
    def change_color(self, color: int):
        self._card_on_field.color = self._POSSIBLE_COLORS[color]
        self._card_on_field.number = 10 # Because it doesnt do anything. 

    def give_card(self, amount, player = None):
        if (player):
            for i in range(amount):
                if self._cards_amount == 0:
                    return False
                if player in self._players:
                    self._players[player].append(self.generate_card())
                    self._cards_amount -= 1
                else:
                    self._players[player] = [self.generate_card()]
        self.player_on_demand = player

    def generate_card(self):
        if random() <= 0.3:
            gen_color = self._POSSIBLE_COLORS[randint(0,3)]
            if gen_color == 'black':
                return SuperCard(gen_color, self._POSSIBLE_ABILITIES[randint(3,4)])
            else:
                return SuperCard(gen_color, self._POSSIBLE_ABILITIES[randint(0,2)])
        else:
            return Card(randint(0,9), self._POSSIBLE_COLORS[randint(0,2)])

    def get_way(self):
        return self._way
    
    def get_cards(self, player):
        return self._players[player]

    def get_field(self):
        return self._card_on_field

    def get_left_cards(self):
        return self._cards_amount

class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

class SuperCard(Card):
    
    def __init__(self, color, ability):
        super().__init__(None, color)
        self.ability = ability

###
