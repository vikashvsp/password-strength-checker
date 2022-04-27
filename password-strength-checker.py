from cmath import exp
import re
def passwordValidator(password):
    if(not(password and password.strip())):
        return 0
    if(bool(re.match(r"^[0-9]*$",password))):
        digit=0.8
    elif(bool(re.match(r"^[a-zA-Z0-9]*$",password))):
        digit=1.5
    elif(bool(re.match(r"^[a-z]*$",password))):
        digit=1.0
    elif(bool(re.match(r"^[a-zA-Z]*$",password))):
        digit=1.3
    elif(bool(re.match(r"^[a-z\-_!?]*$",password))):
        digit=1.3
    elif(bool(re.match(r"^[a-z0-9]*$",password))):
        digit=1.2
    else:
        digit=1.8

    def logF(x):
        return 1.0/(1.0+exp(-x))
    def logC(x):
        return logF((x/2.0)-4.0)
    pass_strength=logC(len(password)*digit)
    return pass_strength
def main():
    password=input("Enter Password\n")
    print(passwordValidator(password))

if __name__ == "__main__":
    main()