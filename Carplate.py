while True: #Loop check until user enters a valid carplate number

      car=input("Enter a carplate number : ")#Get input from user
      car=car.upper()
      if len(car) !=8:    #If carplate number does not have 8 characters
            print("Length validiation check: failed ")
      elif car[0:1] !="S":    #If first letter is not S
            print("Format validation check: failed for left most letter.")
      elif car[2:3].isalpha()==False:    #If 2nd and 3rd characters is not alphabet
            print("Format validation check: failed for 2nd and 3rd letters from the left”.")
      elif car[-1].isalpha()==False:    #Check if the last letter is alphabet from a-z
            print("Format validation check: failed for right most letter")
      elif car[3:7].isdigit()==False:   #Check if the numbers are in fact digits
            print("Format validation check: failed for 4 digits")
      elif int(car [3:7]) <1000 or int(car[3:7]) >9999:    #If number is not between 1000 to 9999
            print("Range  validation  check: failed for the 4 digits")
          
      else:
#assigning integer value to L2 based on the letter inputed
            if car[1]=='A':
                  l2=1
            if car [1]=='B':
                  l2=2
            if car [1]=='C':
                  l2=3
            if car [1]=='D':
                  l2=4
            if car [1]=='E':
                  l2=5
            if car [1]=='F':
                  l2=6
            if car [1]=='G':
                  l2=7
            if car [1]=='H':
                  l2=8
            if car [1]=='I':
                  l2=9
            if car [1]=='J':
                  l2=10
            if car [1]=='K':
                  l2=11
            if car [1]=='L':
                  l2=12
            if car [1]=='M':
                  l2=13
            if car [1]=='N':
                  l2=14
            if car [1]=='O':
                  l2=15
            if car [1]=='P':
                  l2=16
            if car [1]=='Q':
                  l2=17
            if car [1]=='R':
                  l2=18
            if car [1]=='S':
                  l2=19
            if car [1]=='T':
                  l2=20
            if car [1]=='U':
                  l2=21
            if car [1]=='V':
                  l2=22
            if car [1]=='W':
                  l2=23
            if car [1]=='X':
                  l2=24
            if car [1]=='Y':
                  l2=25
            if car [1]=='Z':
                  l2=26
#-----------------------------------------------------------------------------------------------
#assigning integer value to L3 based on the letter inputed

            if car[2]=='A':
                  l3=1
            if car [2]=='B':
                  l3=2
            if car [2]=='C':
                  l3=3
            if car [2]=='D':
                  l3=4
            if car [2]=='E':
                  l3=5
            if car [2]=='F':
                  l3=6
            if car [2]=='G':
                  l3=7
            if car [2]=='H':
                  l3=8
            if car [2]=='I':
                  l3=9
            if car [2]=='J':
                  l3=10
            if car [2]=='K':
                  l3=11
            if car [2]=='L':
                  l3=12
            if car [2]=='M':
                  l3=13
            if car [2]=='N':
                  l3=14
            if car [2]=='O':
                  l3=15
            if car [2]=='P':
                  l3=16
            if car [2]=='Q':
                  l3=17
            if car [2]=='R':
                  l3=18
            if car [2]=='S':
                  l3=19
            if car [2]=='T':
                  l3=20
            if car [2]=='U':
                  l3=21
            if car [2]=='V':
                  l3=22
            if car [2]=='W':
                  l3=23
            if car [2]=='X':
                  l3=24
            if car [2]=='Y':
                  l3=25
            if car [2]=='Z':
                  l3=26

#-----------------------------------------------------------------------------------------------
#Calculating the remainder based on the algorithm

            x=l2*9+l3*4+int(car[3])*5+int(car[4])*4+int(car[5])*3+int(car[6])*2

            remainder=x%19
#-----------------------------------------------------------------------------------------------
#Checking the if the value of the remainder matches up to the number 
            l4=car[7]
            
            if remainder==0:
                  l4='A'
            if remainder==1:
                  l4='Z'
            if remainder==2:
                  l4='Y'
            if remainder==3:
                  l4='X'
            if remainder==4:
                  l4='U'
            if remainder==5:
                  l4='T'
            if remainder==6:
                  l4='S'
            if remainder==7:
                  l4='R'
            if remainder==8:
                  l4='P'
            if remainder==9:
                  l4='M'
            if remainder==10:
                  l4='L'
            if remainder==11:
                  l4='K'
            if remainder==12:
                  l4='J'
            if remainder==13:
                  l4='H'
            if remainder==14:
                  l4='G'
            if remainder==15:
                  l4='E'
            if remainder==16:
                  l4='D'
            if remainder==17:
                  l4='C'
            if remainder==18:
                  l4='B'
#Printing Fail or Pass if l4 equal to the value of the alphabet
            if l4==car[-1]:
                  print("Car  Plate  Number:  Validation  Pass")
                  break
            else:
                  print("Checksum  validation  check: failed for right most letter")
