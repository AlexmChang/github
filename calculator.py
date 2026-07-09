def main():
    x = int(input("What is the value of x?"))
    print("x squared is", square(x))

def square(to="world"):
    return int(to*to)

main()