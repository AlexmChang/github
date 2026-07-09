def main():
    x = int(input("What is the value of x?"))
    print("x squared is", square(x))

def square(n):
    return int(n*n)

main()