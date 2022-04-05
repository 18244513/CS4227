# Cathal Kelly 18244513

from interface_command import ICommand

class ShootCommand(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver
        
    def execute(self):
        self._receiver.run_shoot_command()
        
