state_capitals = {"Washington": "Olympia","Oregon": "Salem", "California": "Sacramento"}

for state in state_capitals:
    print(state)
    # state refers to the key (1st) - aka Washington, etc.

for city in state_capitals.values():
    print(city)
    # This iterates over the values. The city value will be printed - aka Olympia, Salem, etc.

for state in state_capitals:
    print(state_capitals[state], "is the capital of", state)
    # we are iterating over the keys, and using dictionary[key] notation to access the value - 2nd item - aka Olympia, Salem, etc. are the first value.

for state, city in state_capitals.items():
    print(city, "is the capital of", state)
# We can access both the Key and Value names.

