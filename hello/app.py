import os

def path():
    return os.path.abspath(os.path.dirname(__file__))

print(path())