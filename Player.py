class Player:
    def __init__(self, money, name):
        self.money = money
        self.right_player = None
        self.left_player = None
        self.number_of_rolls = 0
        self.name = name
    
    def set_neighbors(self, right_player, left_player):
        """ set the neighbors of the player """
        self.left_player = left_player
        self.right_player = right_player


