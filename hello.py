#ask user for their name
name = input("what is your name? ").strip().title()

# split user name into first and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")