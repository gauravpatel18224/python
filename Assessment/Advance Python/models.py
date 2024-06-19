class User:
    def __init__(self, name, contact, email, gender, city, state, password):
        self.name = name
        self.contact = contact
        self.email = email
        self.gender = gender
        self.city = city
        self.state = state
        self.password = password

class ProductManager(User):
    def __init__(self, name, contact, email, gender, city, state, password):
        super().__init__(name, contact, email, gender, city, state, password)

class Customer(User):
    def __init__(self, name, contact, email, gender, city, state, balance, password):
        super().__init__(name, contact, email, gender, city, state, password)
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance
