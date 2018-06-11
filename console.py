#!/usr/bin/python3
"""
The entry point for the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Our command prompt."""

    def do_quit(self, line):
        """Exits the program."""
        return True
        print("hi")

    def do_EOF(self, line):
        """Exits the program."""
        return True

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = "(hbnb) "
    prompt.cmdloop()
