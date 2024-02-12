#!/usr/bin/python3
"""cmd module to make command interpreter"""


import cmd
import sys
from models.base_model import BaseModel as bs
from models.user import User as us
from models.city import City as ci
from models.state import State as sta
from models.amenity import Amenity as am
from models.review import Review as re
from models.place import Place as pl
from models import storage as st


class HBNBCommand(cmd.Cmd):
    """commands class """
    prompt = "(hbnb) "
    classes_list = ["BaseModel", "User",
                    "City", "State", "Amenity", "Review", "Place"]

    def update(self, line):
        """Updates an instance"""

        line_list = line.split(" ")
        if line:
            line_list = line.split(" ")
            if line_list[0] not in HBNBCommand.classes_list:
                print("** class doesn't exist **")
            elif len(line_list) == 1:
                print("** instance id missing **")
            elif line_list[1]:
                dic = st.all()
                flg = 0
                for key, value in dic.items():
                    if f"{line_list[0]}.{line_list[1]}" == key:
                        if len(line_list) == 2:
                            print("** attribute name missing **")
                            flg = 1
                        elif len(line_list) == 3:
                            print("** value missing **")
                            flg = 1
                        else:
                            if line_list[3][0] == '"':
                                atr_value = line_list[3][1:-1]
                            else:
                                if line_list[3].isdigit():
                                    atr_value = int(line_list[3])
                                else:
                                    atr_value = line_list[3]
                            setattr(value, line_list[2], atr_value)
                            st.save()
                            flg = 1
                            break
                if flg == 0:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def emtylne(self):
        """ execute anything"""

        pass

    def EOF(self, line):
        """command to exit the program"""

        print()
        return True

    def quit(self, line):
        """command to exit the program"""

        return True

    def create(self, line):
        """ new instance"""

        if line:
            if line not in HBNBCommand.classes_list:
                print("** class doesn't exist **")
            else:
                inst = eval(f"{line}()")
                inst.save()
                print(inst.id)
        else:
            print("** class name missing **")

    def show(self, line):
        """string representation of \
            an instance"""

        if line:
            line_list = line.split(" ")
            if line_list[0] not in HBNBCommand.classes_list:
                print("** class doesn't exist **")
            elif len(line_list) == 1:
                print("** instance id missing **")
            elif line_list[1]:
                dic = st.all()
                flag = 0
                for key, value in dic.items():
                    if f"{line_list[0]}.{line_list[1]}" == key:
                        print(value)
                        flag = 1
                        break
                if flag == 0:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def destroy(self, line):
        """Deletes an instance"""

        if line:
            line_list = line.split(" ")
            if line_list[0] not in HBNBCommand.classes_list:
                print("** class doesn't exist **")
            elif len(line_list) == 1:
                print("** instance id missing **")
            elif line_list[1]:
                dic = st.all()
                flag = 0
                for key, value in dic.items():
                    if f"{line_list[0]}.{line_list[1]}" == key:
                        del dic[key]
                        st.save()
                        flag = 1
                        break
                if flag == 0:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def all(self, line):
        """all string representation
           """

        new_list = []
        dic = st.all()
        for value in dic.values():
            new_list.append(str(value))
        if line:
            if line not in HBNBCommand.classes_list:
                print("** class doesn't exist **")
            else:
                print(new_list)
        else:
            print(new_list)

    def default(self, line):
        """specfic commands"""

        if '.' in line:
            dict = st.all()
            cls, method = line.split(".")
            if method == 'all()':
                list_of_clas = []
                for key, val in dict.items():
                    clas_name = str(key).split(".")
                    if cls == clas_name[0]:
                        list_of_clas.append(str(val))
                print(f"[{list_of_clas}]")

            elif method == "count()":
                cnt = 0
                for key, val in dict.items():
                    clas_name = str(key).split(".")
                    if cls == clas_name[0]:
                        cnt += 1
                print(cnt)

            elif method[:6] == "show(\"" and method[-2:] == "\")":
                line = f"{cls} {method[6:-2]}"
                self.show(line)

            elif method[:9] == "destroy(\"" and method[-2:] == "\")":
                line = f"{cls} {method[9:-2]}"
                self.destroy(line)

            elif method[:8] == "update(\"" and method[-1] == ")":
                args = method[7:-1].split(", ", 1)
                if args[1][0] == "{":
                    dictionary = eval(args[1])
                    for key, value in dictionary.items():
                        if type(value) is int:
                            line = f"{cls} {args[0][1:-1]} {key} {value}"
                        else:
                            line = f"{cls} {args[0][1:-1]} {key} \"{value}\""
                        self.update(line)
                else:
                    list_method = method.split(", ")
                    line = f"{cls} {list_method[0][8:-1]} \
{list_method[1][1:-1]} {list_method[2][:-1]}"
                    self.update(line)
            else:
                return cmd.Cmd.default(self, line)
        else:
            return cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
