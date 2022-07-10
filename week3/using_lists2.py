
states = ["Washington", "Oregon", "California"]

# print(states[0])
# print(states[1]) 
# print(states[2])

# print(states[-1])
# print(states[-2])
# print(states[-3])

# states[2] = "Arizona"
# print(states)

# print(len(states))

# states.append("New York")
# print(states)

# states.pop()
# print(states)

# states.pop(1)
# print(states)

for x in states:
    print(x)

for state in states:
    print(state)

for state in states:
    state = state.lower()
    print(state)

print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)

states2 = ['Arizona', 'Ohio', 'Louisiana']

best_states = states + states2

print(best_states)

print(best_states[1:3])
print(best_states[:2])
print(best_states[4:])


