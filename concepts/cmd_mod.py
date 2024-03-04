import cmd, time

class MyCmd(cmd.Cmd):
    prompt = '>> '

    def do_hello(self, arg):
        """Say hello"""
        print("Hello!")

    def help_hello(self):
        """Help for the hello command"""
        print("This command says hello.")

    def do_quit(self, arg):
        """Quit the program"""
        print("Quitting...")
        time.sleep(2)
        return True

if __name__ == '__main__':
    MyCmd().cmdloop()
