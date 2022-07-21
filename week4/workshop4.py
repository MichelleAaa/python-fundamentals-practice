class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, 'has an account balance of:', self.balance)

    def withdraw(self, value):
        self.balance -= float(value)

    def deposit(self, value):
        self.balance += float(value)

    def transfer_money(self, amount, recipient):
        print(f"You are transferring {amount} to {recipient}")
        print('User authentication is required...')
        pin = int(input('Enter your PIN: '))
        if self.pin == pin:
            print('Transfer authorized')
            print(f"Transferring {amount} to {recipient}")
            self.withdraw(amount)
            recipient.deposit(amount)
            return True
        else:
            return False

    def request_money(self, requestee, amount):
        print(f"You are requesting {amount} from {requestee}")
        print('User authentication is required...')
        requestee_pin = int(input(f"Enter {requestee}'s PIN?"))
        if requestee.pin == requestee_pin:
            requestor_password = input('Enter your password: ')
            if self.password == requestor_password:
                requestee.withdraw(amount)
                self.deposit(amount)
                return True
            else:
                return False
        else:
            return False


""" Driver Code for Task 1 """

# bob = User("Bob", 1234, "password")
# print(bob.name, bob.pin, bob.password)

""" Driver Code for Task 2 """

# bob = User("Bob", 1234, "password")
# print(bob.name, bob.pin, bob.password)
# bob.change_name('tom')
# bob.change_pin(5566)
# bob.change_password('testing')
# print(bob.name, bob.pin, bob.password)

""" Driver Code for Task 3"""

# bob = BankUser("Bob", 1234, "password")
# print(bob.name, bob.pin, bob.password, bob.balance)

""" Driver Code for Task 4"""

# bob = BankUser("Bob", 1234, "password")
# bob.show_balance()
# bob.deposit(100)
# bob.show_balance()
# bob.withdraw(50)
# bob.show_balance()

""" Driver Code for Task 5"""

bob = BankUser("Bob", 1234, "password")
mercy = BankUser("Mercy", 4321, "drowssap")
mercy.deposit(5000)
mercy.show_balance()
bob.show_balance()

mercy.transfer_money(500, bob)
mercy.show_balance()
bob.show_balance()

