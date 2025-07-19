import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

password = []

for _ in range(nr_letters):
    password.append(random.choice(letters))
for _ in range(nr_numbers):
    password.append(random.choice(numbers))
for _ in range(nr_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
final_password = ''.join(password)
print(f"Your password is: {final_password}")