import re

def show_homepage():
    print("\n          === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations      |")
    print("------------------------------------------")
    print("|              5.    Exit                    |")
    print("------------------------------------------")

def donate(username):
    donation_amt = float(input('\nEnter amount to donate: '))
    donation_string = f'{username} donated ${donation_amt}'
    print('Thank you for your donation!\n')
    return donation_string

def show_donations(donations):
    print("\n--- All Donations ---")
    if not donations:
        print('Currently, there are no donations.\n')
    else:
        total = 0
        for donation in donations:
            print(donation)
            temp = float(re.findall('[0-9]+.[0-9]+', donation)[0])
            total += temp
        print(f'Total = ${total}')
        print('\n')