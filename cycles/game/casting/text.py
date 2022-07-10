from game.casting.actor import Actor


class Text(Actor):
    """
    
    The responsibility of Text is to display the keys the player has to use .

    """
    def __init__(self,position, player):
        super().__init__()
        self._name = player
        self._points = 0
        self.add_points(0)
        self.set_position(position)


    def add_points(self, points):
        """Adds the text that will be displayed.
        
        """
        self._points += points
        self.set_text(f"{self._name}")
