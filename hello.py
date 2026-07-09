def hello(to="world"):
    print("Hello,", to)


def main():
    #ask user for their name
    name = input("what is your name? ").strip().title()
    hello(name)


main()