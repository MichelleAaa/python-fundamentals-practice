class Bird:
    def __init__(self, name, can_fly):
        self.name = name
        self.can_fly = can_fly

bird = Bird("ostrich", False)

print(bird)

is_tired = True
print("You need to get some sleep" if is_tired else "You are fully rested")
