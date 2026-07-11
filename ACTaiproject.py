def diagnostic():
    print("Welcome to the AI bot that will assist you with your ACT testing. After using this AI your ACT scores will start to go up")
    subject = input(f"Which ACT subject do you need help with? We offer science, math, reading, and english. The subject you need help is? ").strip()
    lvl = input(f"Rank the level of difficulty of problem you want from ACT {subject} on a scale of 1-10 ")
    return lvl, subject

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
    yn = False
    yn = input("Did you answer correctly? (True/False): ")
    return yn

def main():
    lvl, subject = diagnostic()
    lvl = int(lvl)
    prompt(lvl, subject)

    while lvl < 10:
        prompt()
        instruct()
        yn = upddiff()
        if yn == True:
            lvl+=1
            print("Good job! Now the level will be ranked up to", lvl)
        else:
            print("Try again! The level will remain at", lvl)
            
    

    cont = input("Do you want to practice another subject of ACT? True/False ")
    
    if cont:
        main()
        cont = False
    else:
        print("Thank you for using the AI ACT assistant bot")

main()