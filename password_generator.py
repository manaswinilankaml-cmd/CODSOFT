import random
import string

length = int(input("Enter password length: "))

use_upper = input("Include uppercase letters? (y/n): ")
use_lower = input("Include lowercase letters? (y/n): ")
use_digits = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

characters = ""

if use_upper == 'y':
    characters += string.ascii_uppercase

if use_lower == 'y':
    characters += string.ascii_lowercase

if use_digits == 'y':
    characters += string.digits

if use_symbols == 'y':
    characters += string.punctuation

if characters == "":
    print("❌ You must select at least one character type!")
    exit()

password = ""

for i in range(length):
    password += random.choice(characters)

print("\n✅ Generated Password:")
print(password)
