import pyfiglet as pyfiglet

def to_color(string, color):
    color_code = {'blue': '\033[34m',
                    'yellow': '\033[33m',
                    'green': '\033[32m',
                    'red': '\033[31m'
                    }
    return color_code[color] + str(string) + '\033[0m'

result = pyfiglet.figlet_format("JOHN BENEDICT ANDAYA", font = "chiseled" )

print(to_color(result,'blue'))