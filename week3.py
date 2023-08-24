import random

uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters=uppercase_letters.lower()
digits="0123456789"
symbols="=+(){}*/"

uppercase,lower,nums,syms

all=""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length=20
amount=10

for X in range(amount):
    password="".join(random.sample(all, length))
    print(password)
