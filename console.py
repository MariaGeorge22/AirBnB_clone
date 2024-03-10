#!/usr/bin/python3
"""This module contains HBNBCommand class which is
    the entry point of the command interpreter"""
import cmd
import re
from json import loads, dumps
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class contains the entry point of the command interpreter"""

    prompt = "(hbnb) "
    classes_list = ["BaseModel", "User", "State",
                    "City", "Amenity", "Place", "Review"]

    def onecmd(self, line):
        """Can help to handle special commands"""

        parts = re.findall("(.*)[.](.*)[(](.*)[)]", line)
        if parts:
            [class_name, command_name, arguments] = parts[0]
            if re.match(".*[{].*[}]", arguments):
                arguments = arguments\
                    .replace(", ", " $from_dict$ ", 1).replace('"', "", 2)
            else:
                arguments = arguments.replace(", ", " ").replace('"', "", 2)
            return super().onecmd(f"{command_name} {class_name} {arguments}")
        else:
            return super().onecmd(line)

    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Quit command to exit the program"""
        print("Quit command to exit the program.")

    def do_EOF(self, *args):
        """EOF signal to exit the program"""
        return True

    def help_EOF(self):
        """EOF signal to exit the program"""
        print("EOF signal to exit the program.")

    def emptyline(self):
        """Handle the emptyline"""

    def do_create(self, args):
        """create command to Creates a new instance and prints the id"""
        if self.args_check(args, 1):
            obj = storage.create_object(args)()
            obj.save()
            print(obj.id)

    def help_create(self):
        """create command to Creates a new instance and prints the id"""
        print("create command to Creates a new instance and prints the id")

    def do_show(self, args):
        """Prints the string representation of\
        an instance based on the class name and id"""
        obj = self.args_check(args, 2)
        args = args.split(" ")
        if obj:
            print(obj)

    def help_show(self):
        """Prints the string representation of\
            an instance based on the class name and id"""
        print(
            "Prints the string representation of "
            "an instance based on the class name and id"
        )

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        obj = self.args_check(args, 2)
        args = args.split(" ")
        if obj:
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()

    def help_destroy(self):
        """Deletes an instance based on the class name and id"""
        print("Deletes an instance based on the class name and id")

    def do_all(self, args):
        """Prints all string representation of\
            all instances based or not on the class name"""
        if args in HBNBCommand.classes_list:
            print([str(value) for key, value in
                   storage.all().items() if key.count(args)])
        elif args == "":
            print([str(value) for value in
                   storage.all().values()])
        else:
            print("** class doesn't exist **")

    def help_all(self):
        """Prints all string representation of\
            all instances based or not on the class name"""
        print(
            "Prints all string representation of "
            "all instances based or not on the class name"
        )

    def do_count(self, args):
        """Prints the number of all string representation of\
            all instances based or not on the class name"""
        if args in HBNBCommand.classes_list:
            print(
                len([value for key, value in
                     storage.all().items() if key.count(args)])
            )
        elif args == "":
            print(len(storage.all().values()))
        else:
            print("** class doesn't exist **")

    def help_count(self):
        """Prints the number of all string representation of\
            all instances based or not on the class name"""
        print(
            "Prints the number of all string representation of "
            "all instances based or not on the class name"
        )

    def do_update(self, args):
        """Updates an instance based on the class name\
            and id by adding or updating attribute"""
        obj = self.args_check(args, 2)
        args = args.split(" ", 3)
        if not obj:
            return obj
        if len(args) > 2 and args[2]:
            if len(args) > 3 and args[3]:
                self.upadate_value(args[2], args[3], obj)
            else:
                print("** value missing **")
        else:
            print("** attribute name missing **")

    def help_update(self):
        """Updates an instance based on the class name\
            and id by adding or updating attribute"""
        print(
            "Updates an instance based on the class name "
            "and id by adding or updating attribute"
        )

    def upadate_value(self, key, value, obj):
        """Update the attrbute of the object and save it"""
        if key == "$from_dict$":
            for key, value in loads(value.replace("'", '"')).items():
                setattr(obj, key, value)
        else:
            setattr(obj, key, loads(value.replace("'", '"')))
        obj.save()

    @staticmethod
    def args_check(args, max_args):
        """Check if the command arguments is valid or not"""
        args = args.split(" ")
        if args[0] in HBNBCommand.classes_list:
            if max_args == 1:
                return True
        elif args[0] == "":
            return print("** class name missing **")
        else:
            return print("** class doesn't exist **")
        if len(args) > 1 and args[1]:
            obj = storage.all().get(f"{args[0]}.{args[1]}", None)
            if obj:
                if max_args == 2:
                    return obj
            else:
                return print("** no instance found **")
        else:
            return print("** instance id missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
