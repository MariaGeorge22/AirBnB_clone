#!/usr/bin/python3
"""Module providing the command interpreter's entry point."""
# '''' Comment: Reworded for clarity and conciseness.

import re
import cmd
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, line):
        """Handles commands when no other matches are found."""
        # '''' Comment: Clarifies the purpose of the function.
        # print("DEF:::", line)
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to check for class.syntax() format."""
        # '''' Comment: Provides clarity on the function's purpose.
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        class_name = match.group(1)
        cus_method = match.group(2)
        arguments = match.group(3)
        mat_uniqueId_arguments = re.search('^"([^"]*)"(?:, (.*))?$', arguments)
        if mat_uniqueId_arguments:
            uniqueId = mat_uniqueId_arguments.group(1)
            attr_or_dict = mat_uniqueId_arguments.group(2)
        else:
            uniqueId = arguments
            attr_or_dict = False

        arrVal = ""
        if cus_method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(class_name, uniqueId, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                arrVal = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = cus_method + " " + class_name + " " + uniqueId + " " + arrVal
        self.onecmd(command)
        return command

    def update_dictionary(self, class_name, uniqueId, serialized_dict):
        """Helper method for update() with a dictionary."""
        # '''' Comment: Describes the purpose of the function.
        serialized = serialized_dict.replace("'", '"')
        deserialized = json.loads(serialized)
        if not class_name:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif uniqueId is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(class_name, uniqueId)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[class_name]
                for attribute, value in deserialized.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def handle_EOF(self, line):
        """Handles the End Of File character."""
        # '''' Comment: Describes the purpose of the function.
        print()
        return True

    def quit_program(self, line):
        """Exits the program."""
        # '''' Comment: Describes the purpose of the function.
        return True

    def ignore_empty_line(self):
        """Ignores empty lines."""
        # '''' Comment: Describes the purpose of the function.
        pass

    def create_instance(self, line):
        """Creates an instance."""
        # '''' Comment: Describes the purpose of the function.
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            instance = storage.classes()[line]()
            instance.save()
            print(instance.id)

    def show_instance(self, line):
        """Prints the string representation of an instance."""
        # '''' Comment: Describes the purpose of the function.
        if line == "" or line is None:
            print("** class name missing **")
        else:
            parts = line.split(' ')
            if parts[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(parts) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(parts[0], parts[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def delete_instance(self, line):
        """Deletes an instance based on the class name and id."""
        # '''' Comment: Describes the purpose of the function.
        if line == "" or line is None:
            print("** class name missing **")
        else:
            parts = line.split(' ')
            if parts[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(parts) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(parts[0], parts[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def display_all_instances(self, line):
        """Prints string representation of all instances."""
        # '''' Comment: Describes the purpose of the function.
        if line != "":
            parts = line.split(' ')
            if parts[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                my_list = [str(obj) for key, obj in storage.all().items()
                           if type(obj).__name__ == parts[0]]

                print(my_list)
        else:
            my_list = [str(obj) for key, obj in storage.all().items()]
            print(my_list)

    def count_instances(self, line):
        """Counts the instances of a class."""
        # '''' Comment: Describes the purpose of the function.
        parts = line.split(' ')
        if not parts[0]:
            print("** class name missing **")
        elif parts[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    parts[0] + '.')]
            print(len(matches))

    def update_instance(self, line):
        """Updates an instance by adding or updating attributes."""
        # '''' Comment: Describes the purpose of the function.
        if line == "" or line is None:
            print("** class name missing **")
            return

        bla = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(bla, line)
        class_name = match.group(1)
        uniqueId = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif uniqueId is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(class_name, uniqueId)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[class_name]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
