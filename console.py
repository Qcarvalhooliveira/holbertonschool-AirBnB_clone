#!/usr/bin/env python3
"""
Module for the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class for the command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Quit command to exit the program
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
