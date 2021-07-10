#Convert binary to denary
loop = True
while loop == True:
    binaryinput=input("Enter an 8 digit binary number :")#Get input from user
    if len(binaryinput) == 0 :#Validation check(1),presence check
        print("Please enter something")
        continue

    elif len(binaryinput) != 8:#Validation check(2),length check
        print("Please enter 8-digits only")
        continue

    elif binaryinput.isdigit() == False :#Validation check(3),must be digit
        print("Only digits allowed ")
        continue

    for i in range(len(binaryinput)):#Validation check(4),must only contain 0s and 1s
            if int(binaryinput[i]) !=1 and int(binaryinput[i]) !=0 :
                print("Please enter binary number(Only 0 and 1) ")
                break
    else:
        x=0
        for i in range(len(binaryinput)): #for loop
                binaryinput=list(binaryinput) #Turns it into list to find the
                digit=binaryinput.pop() #Takes the last value of the list into variable (digit)
                if digit == '1':
                    x = x + pow(2,i) #Takes the the current i value and raises 2 to that power and adds it to x if it is 1

        print ("The denary value for your input is" , x ,)
               
   

    while True:
        ask=input("Do you want to continue?(Y/N): ")

        if ask.upper()=="Y":
            break
        elif ask.upper()=="N":
            print("Thank you for using this programme")
            loop = False
            break
    
