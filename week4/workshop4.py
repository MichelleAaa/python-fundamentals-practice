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
        print(f"You are transferring ${amount} to {recipient.name}")
        print('Authentication required')
        pin = int(input('Enter your PIN: '))
        if self.pin == pin:
            print('Transfer authorized')
            print(f"Transferring ${amount} to {recipient.name}")
            self.withdraw(amount)
            recipient.deposit(amount)
            return True
        else:
            print('Invalid PIN. Transaction canceled.')
            return False

    def request_money(self, requestee, amount):
        print(f"You are requesting ${amount} from {requestee.name}")
        print('User authentication is required...')
        requestee_pin = int(input(f"Enter {requestee.name}'s PIN: "))
        if requestee.pin == requestee_pin:
            requestor_password = input('Enter your password: ')
            if self.password == requestor_password:
                print('Request authorized')
                print(f'{requestee.name} sent ${amount}')
                requestee.withdraw(amount)
                self.deposit(amount)
                return True
            else:
                print('Invalid password. Transaction canceled.')
                return False
        else:
            print('Invalid PIN. Transaction canceled.')
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
# bob.deposit(1000)
# bob.show_balance()
# bob.withdraw(500)
# bob.show_balance()

""" Driver Code for Task 5"""

bob = BankUser("Bob", 1234, "password")
alice = BankUser("Alice", 5678, "alicepassword")
alice.deposit(5000)
alice.show_balance()
bob.show_balance()

print('\n')
alice.transfer_money(500, bob)
alice.show_balance()
bob.show_balance()

print('\n')
if bob.balance > 0:
    alice.request_money(bob, 250)
    alice.show_balance()
    bob.show_balance()
