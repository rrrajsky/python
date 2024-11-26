
class Dvere:

    def __init__(self, zamceno):
        self.zamceno = zamceno

    def otevrit(self):
        if self.zamceno:
            raise ZamceneDvereException


class ZamceneDvereException(Exception):
    pass

d = Dvere(True)
try:
    d.otevrit()
    print("Prosel jsem")
except ZamceneDvereException as e:
    print("Dvere jsou zamcene, nemuzes je otevrit")