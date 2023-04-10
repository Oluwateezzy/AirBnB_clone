#!/usr/bin/python3
""" command prompt """
import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.reviews import Reviews
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """ command """
    prompt = '(hbnb) '
    classes =  {'BaseModel': BaseModel, 'User': User,
                'City': City, 'State': State,
                'Place': Place, 'Amenity': Amenity,
                'Reviews': Reviews}

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

    def do_create(self, arg):
        """ create instance of model """
        if len(arg) == 0:
            print('** class name missing **')
            return
        if arg:
            lis_arg = arg.split()
            if len(lis_arg) == 1:
                if arg in self.classes.keys():
                    new = self.classes[arg]()
                    new.save()
                    print(new.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """ show instance created """
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg:
            if arg.split()[0] not in self.classes:
                print("** class doesn't exist **")
                return
        if len(arg.split()) > 1:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all():
                val = storage.all()
                print(val[key])
            else:
                 print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """ delete an instance of a classe """
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg:
            if arg.split()[0] not in self.classes:
                print("** class doesn't exist **")
                return
        if len(arg.split()) > 1:
            key = arg.split()[0] + "." + arg.split()[1]
            if key in storage.all():
                value = storage.all()
                del value[key]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        """ all instances in storage """
        if len(arg) == 0:
            print([str(value) for value in storage.all().values()])
        elif arg in self.classes:
            print([str(value) for key, value in storage.all().items() if arg in key])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ update an instances """
        arg =  arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')
if __name__ == '__main__':
    HBNBCommand().cmdloop()
