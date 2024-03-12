import string
import secrets

letters = string.ascii_letters + string.digits + string.punctuation
requiredLength = int(input("How many characters does your password need?\n"))
password = ''

for i in range(requiredLength):
    password += secrets.choice(letters)

print(password)