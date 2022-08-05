#!/usr/bin/python3
""" console.py - HBNBCommand"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    command line interpretor using cmd
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """end of a line
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        raise SystemExit

    def emptyline(self):
        """
        do nothing if empty line is entered
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
