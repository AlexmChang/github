def hello(to):
    print("Hello,", to)


#ask user for their name
name = input("what is your name? ").strip().title()

# split user name into first and last name
hello(name)