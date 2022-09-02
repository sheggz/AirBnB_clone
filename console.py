#!/bin/usr/env python3
"""Custom command line for AirBnB project

This module contains the entry point of the command interpreter
"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "    # a custom prompt

    model_list = ["BaseModel"]

    def do_quit(self, args):
        """Exits the program"""
        return True

    def do_EOF(self, args):
        """Exits the program"""
        return True

    # an empty line + ENTER shouldn’t execute anything
    def emptyline(self):
        return False

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        error = HBNBCommand.handle_errors(args)

        if error:
            return

        obj = eval(args)()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        error = HBNBCommand.handle_errors(args, command="show")

        if error:
            return

        args = args.split(" ")

        objects = storage.all()
        key = ".".join(args)
        obj = objects.get(key)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    # customizing this will help us handle regex inputs
    def onecmd(self, args):
        if args == "quit":
            return self.do_quit(args)
        elif args == "EOF":
            return self.do_EOF(args)
        else:
            return cmd.Cmd.onecmd(self, args)

    @classmethod
    def handle_errors(cls, args, **kwargs):
        if not args:
            print("** class name missing **")
            return True
        else:
            args = args.split(" ")

        n = len(args)
        if args[0] not in HBNBCommand.model_list:
            print("** class does not exists **")
            return True

        if "command" not in kwargs:
            return False

        for arg in kwargs.values():
            if n < 2:
                print("** instance id missing **")
                return True

        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
