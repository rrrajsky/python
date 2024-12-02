
class Flask:
    """
    Class representing a Flask
    """
    def __init__(self, capacity):
        """
        Creates flask of capacity
        :param capacity: in litres
        """
        if type(capacity) != float:
            raise Exception("Invalid type")
        if capacity < 0.5 or capacity > 5.0:
            raise Exception("Invalid capacity")
        self.capacity = capacity
        self.volume = 0.0
        self.isclosed = False

    def __str__(self):
        return f'Flask(capacity: {self.capacity}, current volume: {self.volume}, State: {self.isclosed})'

    def set_volume(self, amount):
        """
        Sets the volume of the flask
        :param amount: in litres
        """
        if self.isclosed == False:
            if type(amount) != float:
                raise Exception("Invalid type")
            if amount < 0.0:
                raise Exception("Invalid capacity")
            if amount > self.capacity:
                amount = self.capacity
            self.volume = amount
        else:
            raise Exception("Flask is closed")

    def empty_the_flask(self):
        """
        Sets the volume of the flask
        to zero
        """
        self.volume = 0.0

    def set_volume_ml(self, amount):
        """
        Sets the volume of the flask
        :param amount: in millilitres
        """
        amount = amount / 1000.0
        self.set_volume(amount)

    def open_flask(self):
        """
        Sets the state of the flask to open
        """
        self.isclosed = False

    def close_flask(self):
        """
        Sets the state of the flask to closed
        """
        self.isclosed = True


# Unit tests
import unittest

class TestFlask(unittest.TestCase):
    def test_initialization(self):

        flask = Flask(3.0)
        self.assertEqual(flask.capacity, 3.0)
        self.assertEqual(flask.volume, 0.0)
        self.assertFalse(flask.isclosed)


        with self.assertRaises(Exception) as e:
            Flask("invalid")
        self.assertEqual(str(e.exception), "Invalid type")


        with self.assertRaises(Exception) as e:
            Flask(0.4)
        self.assertEqual(str(e.exception), "Invalid capacity")

    def test_set_volume(self):
        flask = Flask(3.0)
        flask.open_flask()

        flask.set_volume(1.5)
        self.assertEqual(flask.volume, 1.5)

        flask.set_volume(4.0)
        self.assertEqual(flask.volume, 3.0)

        with self.assertRaises(Exception) as e:
            flask.set_volume("invalid")
        self.assertEqual(str(e.exception), "Invalid type")

        with self.assertRaises(Exception) as e:
            flask.set_volume(-1.0)
        self.assertEqual(str(e.exception), "Invalid capacity")

        flask.close_flask()
        with self.assertRaises(Exception) as e:
            flask.set_volume(1.0)
        self.assertEqual(str(e.exception), "Flask is closed")

    def test_empty_flask(self):
        flask = Flask(3.0)
        flask.open_flask()
        flask.set_volume(2.0)
        flask.empty_the_flask()
        self.assertEqual(flask.volume, 0.0)

    def test_set_volume_ml(self):
        flask = Flask(3.0)
        flask.open_flask()
        flask.set_volume_ml(1500)
        self.assertEqual(flask.volume, 1.5)

    def test_flask_state(self):
        flask = Flask(3.0)
        flask.close_flask()
        self.assertTrue(flask.isclosed)
        flask.open_flask()
        self.assertFalse(flask.isclosed)

unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TestFlask))
