#!/usr/bin/python3
"""
The entry point for the command interpreter interface.
"""

import cmd
from models.base_model import BaseModel
from models import storage
import models
import models.engine


class HBNBCommand(cmd.Cmd):
    """Our command prompt."""

    cls_names = ["BaseModel", "User"]

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
        elif arg == "BaseModel" or arg == "User":
            inst = eval(arg)()
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

    def do_all(self, line):
        """prints all string reps of all instances of all or specified class"""
        all_objs = storage.all()
        args = line.split()

        try:
            cls = args[0]
        except:
            cls = ""

        if cls == "":
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        elif cls not in self.cls_names:
            print("** class doesn't exist **")
        else:
            for key, obj in all_objs.items():
                if obj.__class__.__name__ == cls:
                    print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = ("{}.{}".format(args[0], args[1]))
            new_obj = models.storage.all()
            if key in new_obj.keys():
                del new_obj[key]
            else:
                print("** no instance found **")

    def emptyline(self):
        """ overwrites Cmd.emptyline() """
        pass

    def do_update(self, line):
        """ Updates an instance based on the class name
        and id by adding or updating attribute."""
        args = line.split()
        if len(args) == 3:
            print("** value missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
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
