class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)


class BankUser(User):  # inherits from the User class
    # invokes a built-in Python function called super() to access the __init__ method of the superclass, User, allowing it to initialize the name, email, and password attributes there.
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0
        # adds an instance attribute called balance and initializes it to 0. This attribute only exists in the BankUser class, not in the User class.

    #instance method called check_balance(). This method also only exists in the BankUser class.
    def check_balance(self):
        print(self.name, "has an account balance of:", self.balance) 

#initializes a new instance of BankUser
bankuser1 = BankUser("Jane", "jane@nucamp.co", "bestpassword")

