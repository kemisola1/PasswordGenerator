import random


uppercase_letters = "ABCDSFGTIOHDJFHJFH"
lowercase_letters = "abcdefrgtyhjjljvd"
digits = "012345678"
symbols = "#@%$!&^$?/*&+"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all+= uppercase_letters
if lower:
    all += lowercase_letters 
if nums: 
    all += digits
if syms:
    all += symbols 



length = 10
amount =1

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
