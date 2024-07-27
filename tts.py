import pyttsx3
import sys
print("Jay Swaminarayan")

def main():
    engine = pyttsx3.init()

    while True:
        text = input(" What you want to listen from interpreter : ")
        engine.say(text)
        engine.runAndWait()
        
        next_Move = input("1 for Continue and 2 for exit - ")
        if next_Move == "1":
            continue
        elif next_Move == "2":
            engine.say("You are now exited")
            engine.runAndWait()
            sys.exit(0)
        else :
            print("Please enter only 1 or 2 to move further.")
            sys.exit(0)
    
main()