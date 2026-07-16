def diagnostic(): 
    print("Welcome to the AI bot that will assist you with your ACT testing. After using this AI your ACT scores will start to go up")
    subjectfe = subjectff()

    while True:
        try:
            lvl = int(input(f"Rank the level of difficulty of problem you want from ACT {subjectfe} on a scale of 1-10 "))
            if(lvl<1 or lvl >10):
                print("That is not a valid number! Please try again.")  
            else:
                break  
        except ValueError:
            print("That is not a valid number! Please try again.")  
    return lvl, subjectfe

def whichsubject():
    subjectlist = ["math", "reading", "english", "science"]
    subjects = input(f"Which ACT subject do you need help with? We offer science, math, reading, and english. The subject you need help is? ").strip()  

    return subjects


def subjectff():
    subject = whichsubject()
    subjectlist = ["math", "reading", "english", "science"]

    while True:
        if(subject.casefold() in subjectlist):
            return subject
        else:
            print("That is not a valid subject! The only available subjects are math, reading, english, and science. Please try again. ")
            subject = whichsubject()

def prompt(a, b):
    print("---------- START OF PROMPT ----------")
    print("Create ONE ACT", end=" ")
    print(b, end=" ")
    print("multiple-choice question.")
    print("              Rules:               ")
    print("     1. Ask ONE question. for difficulty", end=" ")
    print(a, end="")
    print("/10")      
    print("     2. Wait for my answer.")  
    print("     3. Grade my answer.")
    print("     4. Explain the answer.")
    print("----------- END OF PROMPT -----------")

def instruct():
    print("• Copy the prompt into ChatGPT.")
    print("• Answer the question.")
    print("• Let ChatGPT grade the answer.")
    input("Press Enter to continue...")

def upddiff():
    yn = input("Did you answer correctly? (True/False): ").title() == "True"
    return yn

def newsubject():
    cont = input("Do you want to practice another subject of ACT? (True/False) ").title() == "True"
    return cont

def main():
    lvl, subject = diagnostic()
    lvl = int(lvl)

    while lvl < 10:
        prompt(lvl, subject)
        instruct()
        yn = upddiff()
        if yn:
            lvl+=1
            print("Good job! Now the level will be ranked up to", lvl)
        else:
            print("Try again! The level will remain at", lvl)

    cont = newsubject()
    
    if cont:
        main()
    else:
        print("Thank you for using the AI ACT assistant bot.")

main()