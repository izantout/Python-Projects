class Bug:
    
    def __init__(self, name, position = [0, 0]):
        self.name = name
        self.position = position
        return
    
    def move_up(self, units):
        # Moves bug up
        self.position[1] += units
        return
    
    def move_down(self, units):
        # Moves bug down
        self.position[1] -= units
        return
    
    def move_left(self, units):
        # Moves bug left
        self.position[0] -= units
        return
    
    def move_right(self, units):
        # Moves bug right
        self.position[0] += units
        return
    
    def __str__(self):
        #returns as string with parethesis for position
        return f"Name: {self.name}\nPosition: {tuple(self.position)}"
