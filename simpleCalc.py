#Michelle
#Simple Calculator

#Init
#Functions
#Adds num1 and num2 and prints result
def add(num1,num2): #function for adding two given numbers
        result = num1 + num2
        print("The result is: " + str(result)) #OR print(result)

def sub(num1,num2): #function for showing the subtracted number
      result = num1 - num2
      print("The result is " + str(result))

def mult(num1,num2): #function for stating product
      result = num1 * num2
      print("The result is " + str(result))

def div(num1,num2): #function for stating the answer
      result = num1 / num2
      print("The result is " + str(result))

def simpleCalc(): #function for calculator intro and adding/subtracting/multiplying/dividing the numbers given
    print ("Welcome Preschoolers to Simple Calculator")
    while True: #looping
        print ("Please choose an operation: ")
        print("""1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit""")
        operation = int(input ("(1-5): "))
        if operation == 1: #for asking and adding numbers
            add1 = int(input("Please input first number: ")) #Make sure to add int since given a number
            add2 = int(input("Please input second number: "))
            add(add1,add2)
        if operation == 2: #for asking and subtracting numbers
            sub1 = int(input("Please input first number: "))
            sub2 = int(input("Please input second number: "))
            sub(sub1,sub2)
        if operation == 3: #for asking and multiplying numbers
            mult1 = int(input("Please input first number: "))
            mult2 = int(input("Please input second number: "))
            mult(mult1,mult2)
        if operation == 4: #for asking and dividing numbers
            div1 = int(input("Please input first number: "))
            div2 = int(input("Please input second number: "))
            div(div1,div2)
        if operation == 5: #to stop the loop
            print("Have a good day!")
            break #stops loop

#Main
simpleCalc()
