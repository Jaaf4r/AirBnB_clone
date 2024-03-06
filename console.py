#!/usr/bin/python3
""" Console """
import cmd
import os


class HBNBCommand(cmd.Cmd):
    """ Console class"""

    prompt = '(hbnb) '  # custom prompt

    def do_help(self, line):
        """
            this method invoked when the user types 'help'
            if line is exists will show a msg, if it's not
            it'll show another msg
        """

        if line.strip() == "quit":
            self.help_quit()
        else:
            print("\nDocumented commands (type help <topic>):\
            \n{}\nEOF  help  quit\n".format('=' * 40))

    def help_quit(self):
        """
            method print a string when invoked
        """

        print("Quit command to exit the program\n")

    def do_quit(self, line):
        """
            this method is invoked when the user types 'quit'
            this method call another method to exists the console
        """
        self.quitted()

    def emptyline(self):
        """
            this method called when the user enters empty line
            without this method we'll have in most cases error
        """
        pass

    def do_cl(self, line):
        """
            method to clear the function by using 'cl' instead of 'clear'
            'cl': command used to clear the console
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def default(self, line):
        """
            This method is called when the user enters
            an unknown command, including EOF.
        """
        if line == 'EOF':
            print("\n", end='')
            self.quitted()

    def quitted(self):
        """
            method to exit the console
        """

        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
