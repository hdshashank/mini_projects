import string
import random

def genpass(n):
    if(n>=6):
        password=''
        for i in range(n):
            password+=''.join(random.choice(pass_list))
        print("\n",password)
    else:
        print("\nPassword should have atleast 6 characters")

while True:
    lower=list(string.ascii_lowercase)
    upper=list(string.ascii_uppercase)
    digits=list(string.digits)
    symbols=list(string.punctuation)
    pass_list=lower+upper+digits+symbols
    n=int(input("\nEnter length(>6) of the password:"))
    genpass(n)
    cont=input("\nDo you want to generate one more password(y/n):")
    if cont.lower()=='n':
        break
    elif cont.lower()=='y':
        continue
    else:
        break 