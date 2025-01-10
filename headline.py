#Clickbait Headline Generator

#init
#Michelle Xilotl
#Pd-4
#10-8-24

#function
def believe_headline(): #creates a string/sentence about a surprising headline
    noun = input("Please enter a noun: ")
    ppronoun = input ("Please enter a possesive pronoun: ")
    place = input("Please enter a place: ")
    print ("You Won't Believe What This " + noun + " Found in " + ppronoun + " " + place)

def top_headline(): #creates a string/sentence using a number and a name
    number = input("Please enter a number between 1-10: ")
    bname = input("Please enter a brand name: ")
    print ("Top " + str(number) + " ways " + bname + " is putting their business into jeopardy")

def celebrity_headline(): #creates a string using numbers and names in variables
    number = input("Please enter a number between 1-10: ")
    cname = input("Please enter a celebrity's name: ")
    drink = input ("Please enter a drink: ")
    print(str(number) + " reasons why " + cname + " loves " + drink)

#main
believe_headline()
top_headline()
celebrity_headline()
