import sys

from .errors import ArgumentError

def main():
    if len(sys.argv) < 2:
        raise ArgumentError("Two few arguments")
    
    print(f"Name is {sys.argv[1]}")