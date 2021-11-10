import os

class Helpers:

    def Clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")