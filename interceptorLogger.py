# Rioghan Lowry 18226531

from interfaceInterceptorLogger import interfaceInterceptorLogger
from contextObject import contextObject
import sys


class interceptorLogger(interfaceInterceptorLogger):
    
    file = open("Coordinates.txt","r+")
    file.truncate(0)
    file.close()

    def log():
        
        original_stdout = sys.stdout
        with open('Coordinates.txt', 'a') as f:
            sys.stdout = f
            contextObject.getXCoords()
            contextObject.getYCoords()
            
            sys.stdout = original_stdout  