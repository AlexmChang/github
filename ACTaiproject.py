def diagnostic():
    print("Welcome to the AI bot that will assist you with your ACT testing. After using this AI your ACT scores will start to go up")
    eng = int(input("What is your English level on a scale of 1-10? "))
    math = int(input("What is your Math level on a scale of 1-10? "))
    reading = int(input("What is your reading level on a scale of 1-10? "))
    science = int(input("What is your science level on a scale of 1-10? "))

    low = min(eng, math, reading, science)
    print("The lowest category from ACT testing is at a level of", low)
    sorted(eng, math, reading, science)
    return 


def ranking(a, b, c, d):
    sorted(a, b, c, d)

def main():
    diagnostic()
    ranking()

main()