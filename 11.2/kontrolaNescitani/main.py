
def scitani(a, b):
    if type(a) == str or type(b) == str:
        raise ValueError("string tam nedavej")
    if type(a) not in (int,float,complex) or type(b) not in (int,float,complex):
        raise TypeError('one of values is not an integer')
    else:
        return a + b

class trida:
    def __init__(self):
        pass

import unittest
class TestScitani(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(scitani(1, 1), 2)
        self.assertEqual(scitani(-1, 1), 0)
        self.assertEqual(scitani(1, -1), 0)
        self.assertEqual(scitani(2, 3), 5)

    def test_real(self):
        self.assertEqual(scitani(3.253, 1.741), 4.994)
        self.assertEqual(scitani(-17.54171,-999.14),-1016.68171)
        self.assertEqual(scitani(-19888, 87451.2), 67563.2)
        self.assertEqual(scitani(1.2, -1.2), 0)

    def test_komp(self):
        self.assertEqual(scitani(3,4j), 3+4j)
        self.assertEqual(scitani(35,8j), 35+8j)
        self.assertEqual(scitani(3j,4j), 7j)
        self.assertEqual(scitani(12j,7), 7+12j)

    # Rozšiřte Unit Test z příkladu 11.1 a přidejte testy, které zkontrolují, že metoda scitani() nesčítá, co sčítat nemá.
    # Metoda má sčítat pouze čísla, tedy ne stringy, ne třídy, ne kolekce, ne booleany, apod.
    # K tomuto účelu se používá metoda assertRaises(), která očekává vyhození výjimky. Například takto:
    def test_bad_input(self):
        t = trida()
        o = trida()
        with self.assertRaises(ValueError):
            scitani("AHOJ", 100)
        with self.assertRaises(ValueError):
            scitani(100, "AHOJ")
        with self.assertRaises(TypeError):
            scitani(None, None)
        with self.assertRaises(TypeError):
            scitani([4, 5, 6], [1, 2, 3])
        with self.assertRaises(TypeError):
            scitani((1,2,3),(4,5,6))
        with self.assertRaises(TypeError):
            scitani(t,o)
        with self.assertRaises(TypeError):
            scitani(True,False)
        with self.assertRaises(ValueError):
            scitani("TRUE",True)
        with self.assertRaises(ValueError):
            scitani(False,"😍")
    # Výše uvedenou metodu přepracujte a rozšiřte o kontrolu všech datových typů a kolekcí,
    # které znáte (např. z kapitoly 1 a 3). Při testování je třeba být velmi kreativní a otestovat všechny možnosti.

if __name__ == '__main__':
    unittest.main()

