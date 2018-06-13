#!/usr/bin/python3
"""
The entry point for the command interpreter interface.
"""

import cmd
from models.base_model import BaseModel
from models import storage
import models
import models.engine
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Our command prompt."""

    cls_names = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

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
        else:
            check = 0
            for item in HBNBCommand.cls_names:
                if item == arg:
                    inst = eval(arg)()
                    inst.save()
                    print(inst.id)
                    check = 1
            if check == 0:
                print("** class doesn't exist **")
                
    def do_show(self, line):
        """ prints string rep of instance based on class and id """
        all_objs = storage.all()
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            check = 0
            for item in HBNBCommand.cls_names:
                if item == args[0]:
                    print("** instance id missing **")
                    check = 1
            if check == 0:
                print("** class doesn't exist **")
        else:
            check = 0
            check2 = 0
            for item in HBNBCommand.cls_names:
                if item == args[0]:
                    check = 1
                    inst = eval(args[0])()
                    for obj_id in all_objs.keys():
                        if str(args[0] + "." + args[1]) == obj_id:
                            check2 = 1
                            obj = all_objs[obj_id]
                            print(obj)
                    if check2 == 0:
                        print("** no instance found **")
            if check == 0:
                print("** class doesn't exist **")

    def do_all(self, line):
        """prints all string reps of all instances of all or specified class"""
        all_objs = storage.all()
        args = line.split()

        try:
            cls = args[0]
        except:
            cls = ""
        check = 0
        if cls == "":
            check = 1
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        else:
            for item in HBNBCommand.cls_names:
                if item == cls:
                    check = 1
                    for key, obj in all_objs.items():
                        if obj.__class__.__name__ == cls:
                            print(obj)
        if check == 0:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = line.split()
        check = 0
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) == 1:
            check = 0
            for item in HBNBCommand.cls_names:
                if item == args[0]:
                    print("** instance id missing **")
                    check = 1
            if check == 0:
                print("** class doesn't exist **")
        else:
            check = 0
            for item in HBNBCommand.cls_names:
                if args[0] == item:
                    check = 1
                    key = ("{}.{}".format(args[0], args[1]))
                    new_obj = models.storage.all()
                    if key in new_obj.keys():
                        del new_obj[key]
                    else:
                        print("** no instance found **")
            if check == 0:
                print("** class doesn't exist **")                

    def do_emptyline(self):
        """ overwrites Cmd.emptyline() """
        pass

    def do_update(self, line):
        """ Updates an instance based on the class name
        and id by adding or updating attribute."""
        all_objs = storage.all()
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            check = 0
            for item in HBNBCommand.cls_names:
                if item == args[0]:
                    print("** instance id missing **")
                    check = 1
            if check == 0:
                print("** class doesn't exist **")
        elif len(args) == 2:
            check = 0
            check2 = 0
            for item in HBNBCommand.cls_names:
                if item == args[0]:
                    check = 1
            if check == 1:
                for obj_id in all_objs.keys():
                    if str(args[0] + "." + args[1]) == obj_id:
                        print("** attribute name missing **")
                        check2 = 1
            if check == 0:
                print("** class doesn't exist **")
            elif check2 == 0:
                print("** no instance found **")
        elif len(args) == 3:
            check = 0
            check2 = 0
            for item in HBNBCommand.cls_names:
                if item == args[0]:
                    check = 1
            if check == 1:
                for obj_id in all_objs.keys():
                    if str(args[0] + "." + args[1]) == obj_id:
                        print("** value missing **")
                        check2 = 1
            if check == 0:
                print("** class doesn't exist **")
            elif check2 == 0:
                print("** no instance found **")
        else:
            all_objs = storage.all()
            class_id = "{}.{}".format(args[0], args[1])
            for obj_id in all_objs.keys():
                if str("BaseModel." + args[1]) == obj_id:
                    setattr(all_objs[class_id], args[2], args[3])
                    all_objs[class_id].save()
                    return
            print("** no instance found **")

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = "(hbnb) "
    prompt.cmdloop()
