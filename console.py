#!/usr/bin/python3
""" command prompt """
import cmd
import sys
import json
import os


class HBNBCommand(cmd.Cmd):
    """ command """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ quit program """
        exit()

    def do_EOF(self, arg):
        """ quit with EOF """
        print('')
        exit()

    def emptyline(self):
        """ emptyline entered """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
