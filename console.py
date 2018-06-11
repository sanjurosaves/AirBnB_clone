#!/usr/bin/python3
"""
The entry point for the command interpreter interface.
"""


import cmd
from models.base_model import BaseModel
from models import storage
import models
import models.engine
import argparse


class HBNBCommand(cmd.Cmd):
    """Our command prompt."""

    def do_quit(self, line):
        """Exits the program."""
        return True
        print("hi")

    def do_EOF(self, line):
        """Exits the program."""
        return True

    def do_create(self, arg):
        """ creates BaseModel instance, saves it to JSON, prints the id """
        if arg == "":
            print("** class name missing **")
        elif arg == "BaseModel":
            inst = BaseModel()
            inst.save()
            print(inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ prints string rep of instance based on class and id """
        all_objs = storage.all()
        args = line.split()
        try:
            cls = args[0]
        except:
            print("** class name missing **")
            return

        try:
            cid = args[1]
        except:
            print("** instance id missing **")
            return

        if cls == "BaseModel":
            inst = BaseModel()
            for obj_id in all_objs.keys():
                if str("BaseModel." + cid) == obj_id:
                    obj = all_objs[obj_id]
                    print(obj)
                    return
            print("** no instance found **")

    def emptyline(self):
        """ overwrites Cmd.emptyline() """
        pass

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = "(hbnb) "
    prompt.cmdloop()
