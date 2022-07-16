def login(database, username, password):
    if username in database and database[username] == password:
        print(f'\nWelcome back {username}!\n')
        return username
    elif username in database and database[username] != password:
        print(f'\nIncorrect password for {username}.\n')
        return ""
    else:
        print('\nUser not found. Please register.\n')
        return ""

def register(database, username, password):
    if username in database:
        print('\nUsername already registered.\n')
        return ""
    elif len(username) > 10:
        print('\nUsername must be under 10 characters in length.\n')
        return ""
    elif len(password) < 5:
        print('\nPassword must be at least 5 characters in length.\n')
        return ""
    else:
        print(f'\nUsername {username} registered!')
        return username