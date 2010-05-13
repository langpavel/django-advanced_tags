from ShellLexer import ShellLexer


ID = 0x01
STRING = 0x02
INT = 0x04
FLOAT = 0x08
DATE = 0x10
TIME = 0x20
TIMESPAN = 0x40
REFERENCE = 0x80

TEXT = ID | STRING
NUM = INT | FLOAT
DATETIME = DATE | TIME


class AdminCommands:
    """
    class maintaining admin shell commands
    """

    AdminCommands.instance = AdminCommands()

    def __init__(self):
        self.commands = []


class AdminCommand:
    """
    Class used inside @admincommand decorator
    """

    def __init__(self, func, *args, **kwargs):
        self.func = func
        AdminCommand._commands += [self]


def admincommand(func, *args, **kwargs):
    "Decorator marker for custom admin shell command"
    AdminCommand(func, *args, **kwargs)
    return func
