#Michelle Xilotl
#1-8-25
#Multiplication Quiz

#initialize
import random
rights = 0 #Variable for how many problems are right
question = 0 #Variable for how many questions the quiz will have

#function
def multi_quiz():
    global rights
    global question
    print("Hello! This is the multiplication quiz!") #intro
    times = int(input("How many questions do you want to take? ")) #asks player for how many questions
    for i in range(times):
        num1 = random.randint(0, 10)
        num2 = random.randint(0,10)
        product = num1 * num2 #Variable for the right answer
        question = question + 1 #adds 1 to the number of questions the player is on
        print("Question " + str(question) + " of " + str(times))
        print("What is " + str(num1) + " x " + str(num2))
        results = int(input("Enter the answer here: ")) #Player inputs answer here
        print("Your answer: " + str(results))
        if results == product: #Tells player if they got it right and adds it to the number of questions right
            rights = rights + 1
            print("Correct!")
        if results != product: #Tells player if they got it wrong
            rights = rights + 0
            print("Incorrect!")
    print("You got " + str(rights) + " out of " + str(question) + " problems right!") #Gives final result


#Main
multi_quiz()
