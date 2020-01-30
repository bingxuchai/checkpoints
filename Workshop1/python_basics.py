"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64



def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if type(num) != int:
        raise TypeError('Please pass in a number')

    return('even' if num % 2 == 0 else 'odd')


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    ans = random.randint(1, 10)
    while 1:
        res = input('Instruction: ')
        if res == 'exit':
            print('exit the game')
            break

        try:
            res = int(res)
            if res < ans:
                print('too low')
            elif res > ans:
                print('too high')
            else:
                print('right')
                break
        except:
            print('please enter your guess or exit')



def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    string = string.lower().replace(' ', '')
    for i in range(int((len(string)/2))):
        if string[i] == string[len(string) - i - 1]:
            continue
        else:
            return False
    return True


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    f = open(filename, 'w')
    username = username.encode('ascii')
    password = password.encode('ascii')
    username = base64.b64encode(username)
    password = base64.b64encode(password)
    f.write('{}\n'.format(username.decode('ascii')))
    f.write('{}\n'.format(password.decode('ascii')))
    f.close()


def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    if password == None:
        f = open(filename, 'r')
        for line in f:
            res = line.encode('ascii')
            res = base64.b64decode(res)
            print(res.decode('ascii'))
    else:
        f = open(filename, 'r+')
        lis = f.readlines()
        f.seek(0)
        password = password.encode('ascii')
        password = base64.b64encode(password)
        f.write(lis[0])
        f.write(password.decode('ascii'))


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
