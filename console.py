#!/usr/bin/python3
"""
Module for the command interpreter
"""
import cmd
from datetime import datetime
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
           "State": State, "City": City, "Amenity": Amenity, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """
    Class for the command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        quit()
        return True

    def do_EOF(self, arg):
        """
        Quit command to exit the program
        """
        quit()
        return True

    def emptyline(self):
        """
        Empty line + ENTER shouldn't execute anything
        """
        return False

    def do_help(self, args):
        """
        Command lists all help details for each command
        """
        cmd.Cmd.do_help(self, args)

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            instance = classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id - save the
        change into the JSON file
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name
        """
        args = shlex.split(arg)
        all_objects = []
        if len(args) == 0:
            for value in storage.all().values():
                all_objects.append(str(value))
            print("[", end="")
            print(", ".join(all_objects), end="")
            print("]")
        elif args[0] in classes:
            for key in storage.all():
                if args[0] in key:
                    all_objects.append(str(storage.all()[key]))
            print("[", end="")
            print(", ".join(all_objects), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                immutable_attrs = ["id", "created_at", "updated_at"]
                if obj:
                    tokens = shlex.split(arg)
                    if len(tokens) < 3:
                        print("** attribute name missing **")
                    elif len(tokens) < 4:
                        print("** value missing **")
                    elif tokens[2] not in immutable_attrs:
                        obj.__dict__[tokens[2]] = tokens[3]
                        obj.updated_at = datetime.now()
                        storage.save()
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
