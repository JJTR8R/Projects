
#Get inputs : Date collected,Class,Num of students
datecollect=input ("enter today's date dd/mm/yy: ")
class1=input("Enter your class : ")
num = int(input("Enter number of students: "))
x=0

#get input 'data; (Index number, temperature)
print("Key in the class index number, folowed by a space.")
print("Key in the temperature.")
for i in range (num):
      data = input ("Enter index number, temperature:")
      data = data.split()

      temp = float(data[1]) #extract temperature from the list

if temp >=38:
      print("The students with fever are", data)
            #process: who has fever,how many has fever

if temp >= 38.0 :
      x=x+1
      print("The number of people with fever is",x)

#process: find average temperature
average=temp/num
print("The average temperature is", average)




      
