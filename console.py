#!/usr/bin/python3
""" Console """
import cmd
import json
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        print()
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]

        try:
            class_instance = globals()[class_name]()
            class_instance.save()
            print(class_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = arg.split()
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in globals() or \
                not issubclass(globals()[args[0]], BaseModel):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        args = arg.split()
        if arg == '':
            print('** class name missing **')
        elif args[0] not in globals() or \
                not issubclass(globals()[args[0]], BaseModel):
            print('** class doesn\'t exist **')
        else:
            if len(args) < 2:
                print('** instance id missing **')
            else:
                classname = args[0]
                objid = args[1]
                key = classname + '.' + objid
                try:
                    del storage.all()[key]
                    storage.save()
                except KeyError:
                    print('** no instance found **')

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        """
        args = arg.split()
        result = []
        if len(args) != 0:
            if args[0] not in globals() or \
                    not issubclass(globals()[args[0]], BaseModel):
                print('** class doesn\'t exist **')
                return
            else:
                for key, value in storage.all().items():
                    if type(value).__name__ == args[0]:
                        result.append(value.__str__())
        else:
            for key, value in storage.all().items():
                result.append(value.__str__())
        print(result)

    def do_update(self, arg):
        ''' Updates an instance based on the class name & id adding/updating
            attribute (save the change into the JSON file). Ex: $ update
            BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com". '''

        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        storage.reload()
        obj = storage.all()

        if args[0] not in globals() or \
                not issubclass(globals()[args[0]], BaseModel):
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = args[0] + "." + args[1]
            obj[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(args) == 2):
            print("** attribute name missing **")
            return
        if (len(args) == 3):
            print("** value missing **")
            return
        obj_dict = obj[obj_key].__dict__
        if args[2] in obj_dict.keys():
            d_type = type(obj_dict[args[2]])
            print(d_type)
            obj_dict[args[2]] = type(obj_dict[args[2]])(args[3])
        else:
            obj_dict[args[2]] = args[3]
        storage.save()

    def do_update2(self, arg):
        ''' Updates an instance based on the class name & id adding/updating
            attribute (save the change into the JSON file). Ex: $ update
            BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com". '''

        if not arg:
            print("** class name missing **")
            return
        my_dict = "{" + arg.split("{")[1]
        args = shlex.split(arg)
        storage.reload()
        obj = storage.all()

        if args[0] not in globals() or \
                not issubclass(globals()[args[0]], BaseModel):
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = args[0] + "." + args[1]
            obj[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (my_dict == "{"):
            print("** attribute name missing **")
            return
        my_dict = my_dict.replace("\'", "\"")
        my_dict = json.loads(my_dict)
        obj_inst = obj[obj_key]
        for k in my_dict:
            if hasattr(obj_inst, k):
                d_type = type(getattr(obj_inst, k))
                setattr(obj_inst, k, my_dict[k])
            else:
                setattr(obj_inst, k, my_dict[k])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
