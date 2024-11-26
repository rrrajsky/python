
class Flask:
    """
    CLass representing a flask
    """

    def __init__(self, capacity):
        """
        Creates a flask of capacity and amount of 0
        :param capacity: in liters
        """
        if type(capacity) != float:
            raise Exception("Capacity must be float")
        if 0 >= capacity > 5:
            raise Exception("Capacity must be between 0 and 5")


        self.capacity = capacity
        self.amount = 0
        self.closed = False

    def __str__(self):
        """
        Returns a string representation of the object
        :return:
        """
        return f'Flask(capacity: {self.capacity}, amount: {self.amount}, closed: {self.closed})'

    def get_amount(self):
        """
        Gets the amount of liquid in liters in the flask
        :return:
        """
        return self.amount

    def set_amount(self, amount):
        """
        Sets the amount of liquid in liters in the flask if the flask is opened
        :param amount: in liters
        :return:
        """
        if not self.closed:
            if type(amount) != float:
                raise Exception("Amount must be float")
            if amount > self.capacity:
                raise Exception("Amount must be less than capacity")

            self.amount = amount
        else:
            raise Exception("Flask is closed")

    def get_amount_in_milliliters(self):
        """
        Gets the amount of liquid in the flask in milliliters
        :return:
        """
        return self.get_amount()*1000

    def set_amount_in_milliliters(self, amount):
        """
        Sets the amount of liquid in the flask in milliliters
        :param amount: in milliliters
        :return:
        """
        amount = amount/1000
        self.set_amount(amount)

    def empty(self):
        """
        Empties the flask
        :return:
        """
        self.set_amount(0.0)

    def close(self):
        """
        Closes the flask
        :return:
        """
        self.closed = True

    def open(self):
        """
        Opens the flask
        :return:
        """
        self.closed = False
flaska = Flask(1.0)
print(flaska)
flaska.set_amount(0.5)
print(flaska)
flaska.empty()
print(flaska)
flaska.set_amount_in_milliliters(872.0)
print(flaska)