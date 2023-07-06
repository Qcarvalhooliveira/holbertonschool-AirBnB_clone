#!/usr/bin/python3
"""
Module for the command interpreter
"""
import cmd
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

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances based or not
        on the class name.
        """
        args = arg.split()
        obj_dict = storage.all()
        if not args:
            print([str(obj_dict[key]) for key in obj_dict])
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            print([str(obj_dict[key]) for key in obj_dict if
                  key.startswith(args[0])])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating an attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
