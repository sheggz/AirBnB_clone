#!/usr/bin/env python3
"""HBNBCommand Class.

Custom command line for AirBnB project.
"""
import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    models = ("Amenity",
              "BaseModel",
              "City",
              "Place",
              "Review",
              "State",
              "User")

    def do_quit(self, arg):
        """Quit command to exit the program

        """
        return True

    def do_EOF(self, arg):
        """Exits the program when user calls EOF

        """
        return True

    def emptyline(self):
        # Overrides the dafult repeating of previous command
        return False

    def do_create(self, arg):
        """Creates a new instance of a class, saves it and prints the id

        """
        error = HBNBCommand.HBNBCommand_error_handler(arg)
        if error:
            return

        obj = eval(arg)()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an object based on the class
name and id

        """
        error = HBNBCommand.HBNBCommand_error_handler(arg, command="show")
        if error:
            return

        arg = arg.split()
        objects = storage.all()
        key = f"{arg[0]}.{arg[1]}"
        obj = objects.get(key)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an object based on the class name and id

        """
        error = HBNBCommand.HBNBCommand_error_handler(arg, command="destroy")

        if error:
            return

        arg = arg.split()
        key = f"{arg[0]}.{arg[1]}"
        objects = storage.all()
        if key in objects and storage.delete(objects[key]):
            pass
        else:
            print("** instance not found **")

    def do_all(self, arg):
        """Prints string representation of all objects based on or not
the class name

        """
        error = HBNBCommand.HBNBCommand_error_handler(arg, command="all")

        if error:
            return

        arg = arg.split(" ")
        objects = storage.all()
        if arg[0] == "":
            for obj in objects.values():
                print(obj)
        else:
            for key in objects:
                obj_key = key.split(".")
                if obj_key[0] == arg[0]:
                    print(objects[key])

    def do_update(self, arg):
        """Updates an object based on the class name and id by adding a new
attribute or by updating an already existing attribute

        """
        error = HBNBCommand.HBNBCommand_error_handler(arg, command="update")

        if error:
            return

        arg = arg.split()
        class_name = arg[0]
        obj_id = arg[1]
        attr_name = arg[2]
        attr_value = arg[3]

        if "\"" in attr_value:
            attr_value = attr_value[1:-1]

        if attr_value.isdigit():
            attr_value = int(attr_value)

        objects = storage.all()
        key = f"{class_name}.{obj_id}"

        for obj_key in objects:
            if obj_key == key:
                obj = objects[obj_key]
                setattr(obj, attr_name, attr_value)
                obj.save()
                return

        print("** instance id not found **")

    def onecmd(self, args):
        if args == "quit":
            return self.do_quit(args)
        elif args == "EOF":
            return self.do_EOF(args)
        else:
            return cmd.Cmd.onecmd(self, args)

    @classmethod
    def HBNBCommand_error_handler(cls, arg, **kwargs):
        if "all" in kwargs.values():
            if not arg:
                return False

        if not arg:
            print("** class name missing **")
            return True
        else:
            arg = arg.split()

        number_of_command_arg = len(arg)
    
        if arg[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
            return True

        if "command" not in kwargs:
            return False
        
        for command_arg in kwargs.values():
            if command_arg in ["show", "destroy"]:
                if number_of_command_arg < 2:
                    print("** instance id missing **")
                    return True

            if command_arg == "update":
                if number_of_command_arg < 2:
                    print("** instance id missing **")
                    return True
                elif number_of_command_arg < 3:
                    print("** attribute name missing **")
                    return True
                elif number_of_command_arg < 4:
                    print("** value missing **")
                    return True

        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
