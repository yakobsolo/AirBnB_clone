#!/usr/bin/python3
""" console.py - HBNBCommand"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    command line interpretor using cmd
    """
    prompt = "(hbnb) "
    cls = {"BaseModel": BaseModel, "User": User}

    def do_EOF(self, line):
        """end of a line
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        raise SystemExit

    def emptyline(self):
        """
        do nothing if empty line is entered
        """
        pass

    def do_create(self, line):
        """create a ne instance of basemodel
        save it to json and prints the id
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.cls.keys():
            print("** class doesn't exist **")
        else:
            obj1 = HBNBCommand.cls[line]()
            obj1.save()
            print(obj1.id)

    def do_show(self, line):
        """print the string representation of an instance
        based on the class name and id
        """
        list_of_line = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif list_of_line[0] not in HBNBCommand.cls.keys():
            print("** class doesn't exist **")
            return
        elif len(list_of_line) == 1:
            print("** instance id missing **")
            return
        else:
            key_of_instance = list_of_line[0] + "." + list_of_line[1]
            all_instances = storage.all()
            if key_of_instance not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[key_of_instances]
                print(obj)

    def do_destroy(self, line):
        """deletes an instance base onthe class name
        and id
        """
        list_of_line = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif list_of_line[0] not in HBNBCommand.cls.keys():
            print("** class doesn't exist **")
            return
        elif len(list_of_line) == 1:
            print("** instance id missing **")
            return
        else:
            key_of_instances = list_of_line[0] + "." + list_of_line[1]
            all_instances = storage.all()
            if key_of_instances not in all_instances.keys():
                print("** no instance found **")
            else:
                del (all_instances[key_of_instances])
                storage.save()

    def do_all(self, line):
        """prints all string representation of all instances based
        or not on class name
        """
        obj_list = []
        objs = storage.all()
        try:
            if len(line) != 0:
                eval(line)
            else:
                pass
        except NameError:
            print("** class doesn't exist **")
            return
        line.strip()
        for key, val in objs.items():
            if len(line) != 0:
                if type(val) is eval(line):
                    val = str(objs[key])
                    obj_list.append(val)
            else:
                val = str(objs[key])
                obj_list.append(val)
        print(obj_list)

    def do_update(self, line):
        """updates an instance based on the
        class name and id by
        adding or updating attribute
        """
        list_of_line = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif list_of_line[0] not in HBNBCommand.cls.keys():
            print("** class doesn't exist **")
            return
        elif len(list_of_line) == 1:
            print("** instance id missing **")
            return
        elif len(list_of_line) == 2:
            print("** attribute name missing **")
        elif len(list_of_line) == 3:
            print("** value missing **")
        else:
            key_of_instances = list_of_line[0] + "." + list_of_line[1]
            all_instances = storage.all()
            if key_of_instances not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[key_of_instances]
                setattr(obj, list_of_line[2], list_of_line[3])
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
