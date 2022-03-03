class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver
        
    def process(self):
        pass
    
class MoveCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver
        
    def process(self):
        self.receiver.perform_action()
        
class Receiver:
    def perform_action(self):
        print('Action performed in receiver')
        
class Invoker:
    def command(self, cmd):
        self.cmd = cmd
        
    def execute(self):
        self.cmd.process()
        
if __name__ == "__main__":
    receiver = Receiver()
    cmd = MoveCommand(receiver)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()