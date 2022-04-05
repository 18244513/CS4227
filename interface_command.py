# Cathal Kelly 18244513

from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute():
        "The required execute method that all command objects will use"
        
    