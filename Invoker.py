# Cathal Kelly 18244513

class Invoker:
    "The Invoker Class"
    def __init__(self):
        self._commands = {}
        
    def register(self, command_name, command):
        "Register commands in the Invoker"
        self._commands[command_name] = command
        
    def execute(self, command_name):
        "Execute any registered commands"
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print("Command ["+ command_name + "] not recognised")
    