# Cathal Kelly 18244513

from cmath import rect
from interface_command import ICommand

class MoveUpCommand(ICommand):
    def __init__(self, tank):
        self._tank = tank
        
    def execute(self):
        self._tank.run_move_up_command()
        
class MoveDownCommand(ICommand):
    def __init__(self, tank):
        self._tank = tank
        
    def execute(self):
        self._tank.run_move_down_command()

class MoveRightCommand(ICommand):
    def __init__(self, tank):
        self._tank = tank
        
    def execute(self):
        self._tank.run_move_right_command()
        
class MoveLeftCommand(ICommand):
    def __init__(self, tank):
        self._tank = tank
        
    def execute(self):
        self._tank.run_move_left_command()