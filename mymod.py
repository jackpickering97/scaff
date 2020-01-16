# This is a module - I want to stop people executing it directly
# When imported, the value of __name__ will be the module name (not '__main__').
import sys


if __name__ == '__main__':
    sys.exit()

def my_func():
    pass

print(__name__)
